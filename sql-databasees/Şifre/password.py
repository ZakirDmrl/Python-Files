import hashlib

def generate_dynamic_password(username, password):
    # Kullanıcı adı ve parolayı birleştirerek özel bir metin oluşturuyoruz
    combined_text = username + password

    # Özel metni bir özet fonksiyonu kullanarak karmaşıklığı artırıyoruz
    hashed_text = hashlib.sha256(combined_text.encode()).hexdigest()

    # Şifre oluşturmak için bazı özet değerlerini alıyoruz
    first_part = hashed_text[:4]
    second_part = hashed_text[4:8]

    # Şifreyi oluşturuyoruz
    dynamic_password = first_part.upper() + "-" + second_part.lower()

    return dynamic_password

# Kullanıcı adı ve parolayı alalım
username = input("Kullanıcı adınızı girin: ")
password = input("Parolanızı girin: ")

# Dinamik şifreyi oluşturalım
dynamic_password = generate_dynamic_password(username, password)

# Sonuçları yazdıralım
print("Dinamik Şifre:", dynamic_password)
