file = open("newfile.txt","w",encoding="utf-8")
file.write("SELAMUN ALEYKÜM")

file.close()
with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(3)
    print(file.tell())
    content2 = file.read()
    print(content2)