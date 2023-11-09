import cv2
import numpy as np

def main():
    None


def goruntuOkuma():
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