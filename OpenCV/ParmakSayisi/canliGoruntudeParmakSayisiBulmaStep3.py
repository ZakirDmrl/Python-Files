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
    kutu_sol_ust = (50, 50)
    kutu_sag_alt = (250, 300)
    kutu_icindeki_konturlar = []
    konturlar, _ = cv2.findContours(maske.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.rectangle(goruntu, kutu_sol_ust, kutu_sag_alt, (100, 23, 10), 3)


    for kontur in konturlar:
        alan = cv2.contourArea(kontur)
        x, y, w, h = cv2.boundingRect(kontur)
        if alan > 1000 and kutu_sol_ust[0] < x < kutu_sag_alt[0] and kutu_sol_ust[1] < y < kutu_sag_alt[1]:  # Belirli bir alan eşiği ayarlayın
            # El konturunu çizdirin
            kutu_icindeki_konturlar.append(kontur)

    for kontur in kutu_icindeki_konturlar:
        x, y, w, h = cv2.boundingRect(kontur)
        cv2.drawContours(goruntu, [kontur], -1, (0, 255, 0), 2) # parmakları çiz
        cv2.rectangle(goruntu, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        cv2.putText(goruntu, "Eliniz Alginaldi", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # Convex Hull ile dışbükey kabarcıkları ve dışbükey noktaları belirleyin
        disbukeyKabarciklar = cv2.convexHull(kontur, returnPoints=False)
        disbukeyNoktalar = cv2.convexHull(kontur, returnPoints=True)
        # Dışbükey kabarcıkların indekslerini bir dizi olarak alın
        disbukeyKabarciklar = np.array(disbukeyKabarciklar)
        siraliDisbukeyKabarciklar = np.sort(disbukeyKabarciklar) 
        # Alanlarına göre büyükten küçüğe sıralayın
        # Alanlarına göre büyükten küçüğe sıralayın
        # alanlar = [cv2.contourArea(konturlar[x[0]]) for x in disbukeyKabarciklar]
        # sirali_indeksler = np.argsort(alanlar)[::-1]
        # disbukeyKabarciklar = disbukeyKabarciklar[sirali_indeksler]

        print("disbukeyKabarciklar uzunluğu:", len(disbukeyKabarciklar))
        print("disbukeyNoktalar uzunluğu:", len(disbukeyNoktalar))
        

        for i in range(1, len(siraliDisbukeyKabarciklar)):

            print("disbukeyKabarciklar değeri:",siraliDisbukeyKabarciklar[i])
            print("disbukeyNoktalar değeri:",disbukeyNoktalar[i])



        # # Parmak sayısını belirleyin
        # parmak_sayisi = 1  # En büyük kabarcık bir parmağı temsil eder
        # eşik_mesafe = 10  # İki kabarcık arasındaki eşik mesafe
        # for i in range(1, len(disbukeyKabarciklar)):
        #     indeks_i = disbukeyKabarciklar[i]
        #     kontur_i = konturlar[indeks_i]
        #     for j in range(i + 1, len(disbukeyKabarciklar)):
        #         indeks_j = disbukeyKabarciklar[j]
        #         kontur_j = konturlar[indeks_j]
                
        #         mesafe = np.linalg.norm(
        #             (cv2.moments(kontur_i)['m10'] / cv2.moments(kontur_i)['m00'],
        #             cv2.moments(kontur_i)['m01'] / cv2.moments(kontur_i)['m00']),
        #             (cv2.moments(kontur_j)['m10'] / cv2.moments(kontur_j)['m00'],
        #             cv2.moments(kontur_j)['m01'] / cv2.moments(kontur_j)['m00']))
        
        # if mesafe > eşik_mesafe:
        #     parmak_sayisi += 1

        
        # if mesafe > eşik_mesafe:
        #     parmak_sayisi += 1



        #     cv2.putText(goruntu, f"Parmak Sayisi: {parmak_sayisi}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    cv2.imshow("Kamera", goruntu)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()