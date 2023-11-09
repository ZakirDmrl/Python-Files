import cv2
import mediapipe as mp
import serial # Arduino için

ser = serial.Serial("COM4",9600)
kamera = cv2.VideoCapture(0)
cizim = mp.solutions.drawing_utils
el_mod = mp.solutions.hands

with el_mod.Hands(static_image_mode = True) as eller:
    while True:
        ret,frame = kamera.read()
        frame = cv2.flip(frame,1) # kamera da aynalama işlemi yapıp ters görüntüyü düzelttim.
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) # bgr olarak gelen frame i rgb ye çevirdim
        result = eller.process(rgb) 

        yukseklik,genislik,_ = frame.shape
        
        if result.multi_hand_landmarks:
            for ellandmark in result.multi_hand_landmarks:
                for koordinat in el_mod.HandLandmark:
                    koordinat1 = ellandmark.landmark[4] # burada 4 baş parmak 8 işaret parmak 20 serçe parmak
                    koordinat2 = ellandmark.landmark[20]
                    cv2.circle(frame,(int(koordinat1.x*genislik),int(koordinat1.y*yukseklik)),6,(0,0,255),-1) 
                    cv2.circle(frame,(int(koordinat2.x*genislik),int(koordinat2.y*yukseklik)),6,(0,0,255),-1)
                    cv2.line(frame,(int(koordinat1.x*genislik),int(koordinat1.y*yukseklik)),(int(koordinat2.x*genislik),int(koordinat2.y*yukseklik)),(255,0,0),3)
                    mesafe = int(abs(koordinat2.x-koordinat1.x)*genislik) # x koordinatları arasındaki mesafe hesaplandı (abs sol el için gelen - değerleri + yapmak için)
                    # print(mesafe)
                    cv2.putText(frame,"Mesafe: "+str(mesafe),(80,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    if mesafe > 220:
                        ser.write("A",encode())
                    elif mesafe > 180:
                        ser.write("B",encode())
                    elif mesafe > 140:
                        ser.write("C",encode())
                    elif mesafe > 100:
                        ser.write("D",encode())
                    elif mesafe > 60:
                        ser.write("E",encode())
                    elif mesafe > 20:
                        ser.write("F",encode())
                    else:
                        ser.write("G",encode())

                        
        cv2.imshow("goruntu",frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
kamera.release()
cv2.destroyAllWindows()