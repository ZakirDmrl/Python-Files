class Arac:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.yakit_tipi = "Benzin" if marka == "Ford" else "Bilinmiyor"

    def hareket_et(self):
        print("Araç hareket ediyor.")

    def bilgi_goster(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Yakıt Tipi: {self.yakit_tipi}")

# Arac sınıfından nesne oluşturma
arac1 = Arac("Ford", "Focus")
arac1.hareket_et()
arac1.bilgi_goster()
# Çıktı:
# Marka: Ford
# Model: Focus
# Yakıt Tipi: Benzin

arac2 = Arac("Toyota", "Corolla")
arac2.hareket_et()
arac2.bilgi_goster()
# Çıktı:
# Marka: Toyota
# Model: Corolla
# Yakıt Tipi: Bilinmiyor
