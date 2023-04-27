# error handing => Hata yönetimi


# except ZeroDivisionError:
#     print('y için 0 girilemez')
# except ValueError:
#     print('char değer girilemez.')
    # or genel olarak ortak hata mesajı yazılabilir
# except:
#     print('yanlış bilgi girdiniz.')
# except (ZeroDivisionError,ValueError) as e:
#     print('yanlış bilgi girdiniz.')
    # print(e)
# while True: # Doğru bilgiyi girene kadar input ve hata mesajı verir alır 
#     try:
#         x= int(input('x: '))
#         y= int(input('y: '))
#         print(x/y)
#     except Exception as ex:
#         print('yanlış bilgi girdiniz.', ex)
#     else:
#         break
#     finally:
#         print('try except sonlandı.')

# HATA YÖNETİMİ2 - Raising an Exception
def check_password(psw):
    import re # regular exprection 
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harf içermeli")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf içermeli")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam içermeli")
    elif not re.search("[|@$]",psw):
        raise Exception("parola alpha numaric karakter içermeli")
    elif re.search("\s",psw): # İMPORT
        raise Exception("parola  boşluk içermemeli")
    else:
        print('Geçerli numara.metod')
password = '1414233aA@'
try:
   check_password(password)
except Exception as ex:
    print(ex)
else:
    print('Geçerli numara.else')
finally:
    print('Validation tamamlandı')
