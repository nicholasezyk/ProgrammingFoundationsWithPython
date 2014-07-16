import turtle

def branches(length, depth):
    window = turtle.Screen()
    window.bgcolor("blue")
    chihiro = turtle.Turtle()
    chihiro.color("orange")
    chihiro.speed(5)

    degree = 30

    if (length <= 1 || depth == 0):
        window.exitonclick()
        return

    else:
        chihiro.forward(length)
        chihiro.left(180)
        chihiro.forward(length * .4)
        chihiro.left(180 - degree)
        branches(length * .6, depth - 1)


    window.exitonclick()
    
branches(100, 15)

   
