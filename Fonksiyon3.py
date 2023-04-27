ZakirHesap = {
    'HesapNo': '123456',
    'HesapSahibi' : 'Muhammed Zakir Demirel',
    'bakiye' : 3000,
    'ekhesap' : 2000
}

AliHesap = {
    'HesapNo': '123256',
    'HesapSahibi' : 'Muhammed Ali Kan',
    'bakiye' : 4000,
    'ekhesap' : 2000
}

def ParaCek(hesap,miktar):
    print(f"Merhaba {hesap['HesapSahibi']}")
    if miktar < hesap['bakiye']:
        hesap['bakiye'] -= miktar
        print('Paranizi cekebilirsiniz')
    else:
        toplam = hesap['bakiye'] + hesap['ekhesap']
        if(toplam > miktar):
            kullan = input('Ekhesap kullanilsin mi?(e/h)')
            if kullan == 'e': 
                toplam -= miktar
                print('Paranizi cekebilirsiniz')
            else:
                print(f"{hesap['HesapNo']} nolu  hesabinizad {toplam} para vardir.")
        else:
            print('Yetersiz miktar.')

ParaCek(ZakirHesap,6000)