from graphics import *

def main():
    # Create a graphical window with a size of 500x500 pixels
    myCanvas = GraphWin("Flower", 500, 500)

    # Set the background color to green
    myCanvas.setBackground("green")

    # Create and draw a simple rectangle (sky)
    sky = Rectangle(Point(0, 0), Point(500, 400))
    sky.setFill("light blue")
    sky.draw(myCanvas)

    # Create and draw a simple line (stem)
    stem = Line(Point(250, 200), Point(250, 450))
    stem.setWidth(5)
    stem.setFill("dark green")
    stem.draw(myCanvas)

    # Create and draw an ellipse (flower)
    flower = Oval(Point(175, 150), Point(325, 225))
    flower.setFill("orange")
    flower.draw(myCanvas)

    # Create and draw a circle (flower center)
    center = Point(250, 187.5)
    radius = 15
    circle = Circle(center, radius)
    circle.setFill("yellow")
    circle.draw(myCanvas)
    

    # Wait for the user to click on the window before closing it
    myCanvas.getMouse()
    myCanvas.close()

if __name__ == "__main__":
    main()
