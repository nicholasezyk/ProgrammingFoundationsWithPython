import turtle

def branches(length, depth):
    window = turtle.Screen()
    window.bgcolor("blue")
    chihiro = turtle.Turtle()
    chihiro.color("orange")
    chihiro.speed(5)

    degree = 30

    while (length > 0 and depth > 0):
        chihiro.forward(length)
        chihiro.left(180)
        chihiro.forward(length * .3)
        chihiro.left(180 - degree)

        length = length * .9
        depth = depth - 1


    window.exitonclick()
    
branches(125, 125)
