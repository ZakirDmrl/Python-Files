import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret, goruntu = camera.read()

    # Görüntüyü BGR'den HSV'ye dönüştürün
    hsv_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)

    # Renk sınırlaması ile eli ayırın (örnek olarak yeşil renk)
    lower_skin = np.array([0, 20, 80], dtype="uint8")
    upper_skin = np.array([20, 255, 255], dtype="uint8")

    maske = cv2.inRange(hsv_goruntu, lower_skin, upper_skin)

    # Erosion ve dilation işlemleri uygulayarak gürültüyü azaltın
    kernel = np.ones((5, 5), np.uint8)
    maske = cv2.erode(maske, kernel, iterations=1)
    maske = cv2.dilate(maske, kernel, iterations=1)

    # Kontur tespiti yapın
    konturlar, _ = cv2.findContours(maske.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    kutu_icindeki_konturlar = []
    # Kutu yapımı 
    kutu_sol_ust = (50, 50)
    kutu_sag_alt = (250, 300)
    cv2.rectangle(goruntu, kutu_sol_ust, kutu_sag_alt, (100, 23, 10), 3)
    for kontur in konturlar:
        alan = cv2.contourArea(kontur)
        x, y, w, h = cv2.boundingRect(kontur)
        
        if alan > 1000 and kutu_sol_ust[0] < x < kutu_sag_alt[0] and kutu_sol_ust[1] < y < kutu_sag_alt[1]:

            kutu_icindeki_konturlar.append(kontur)

    for kontur in kutu_icindeki_konturlar:
        x, y, w, h = cv2.boundingRect(kontur)

        # Eliniz olan bölgeyi yeşil bir dikdörtgenle çerçeveleyin
        cv2.rectangle(goruntu, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(goruntu, "Eliniz Alginaldi", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.putText(goruntu, "Elinizi Kutunun Icinde Yerlestirin", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), thickness=3)

    cv2.imshow("Kamera", goruntu)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
