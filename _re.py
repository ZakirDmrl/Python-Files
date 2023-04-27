import re
result = dir(re)

#re module
str = "Python Kursu: Python Programlama Rehberiniz"
result = re.findall("Python",str) 
result =len(result)
result = re.split(" ",str)
result = re.sub(" ","-",str) #Boşluk karakteri - ile değiştirildi.
result = re.search("Python",str) # Sadece ilk bulduğunu söyler
result = result.span()

#regular expression


print(result)


