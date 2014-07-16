import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")
    chihiro = turtle.Turtle()
    chihiro.color("orange")
    chihiro.speed(5)

    length = 20
    sides = 3

    while (sides < 25)
        deg = (sides - 2) * 180 / sides
        deg = 180 - deg

        s = 0
        while (s < sides)
            chihiro.forward(length)
            chihiro.left(deg)
            s = s + 1

        length = length + 20


    window.exitonclick()
    


draw_square()    
