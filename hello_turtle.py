import turtle

def draw_petal():
    """this function creates a single petal"""
    turtle.circle(100,90)
    turtle.left(90)
    turtle.circle(100,90)
    return

def draw_flower():
    """this function creates one flower by using the "draw_petal" function"""
    turtle.setheading(0)
    draw_petal()
    turtle.setheading(90)
    draw_petal()
    turtle.setheading(180)
    draw_petal()
    turtle.setheading(270)
    draw_petal()
    turtle.setheading(270)
    turtle.forward(250)
    return

def draw_flower_advance():
    """this function paints a single flower and also moves the turtle head to
    allow drawing of additional flowers"""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.down()
    return

def draw_flower_bed():
    """this function creates a garden with 3 flowers"""
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_advance()
    draw_flower_advance()
    draw_flower_advance()
    return


if __name__ == "__main__" :
    draw_flower_bed()
    turtle.done
