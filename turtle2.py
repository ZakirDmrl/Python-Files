import turtle
ok = turtle.Turtle()

def kareCiz(uzunlluk):
    for i in range(4):
        ok.forward(uzunluk)
        ok.right(90)

def ucgenCiz(uzunluk):
    for a in range(3):
        ok.forward(200)
        ok.left(120)

for a in range(5):
    kareCiz(50)
    ok.forward(50)
