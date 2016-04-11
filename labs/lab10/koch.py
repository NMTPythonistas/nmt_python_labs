import turtle

def koch_line(width, depth=0):
    if depth <= 0:
        turtle.forward(width)
    else:
        koch_line(width / 3, depth - 1)
        turtle.left(60)
        koch_line(width / 3, depth - 1)
        turtle.right(2 * 60)
        koch_line(width / 3, depth - 1)
        turtle.left(60)
        koch_line(width / 3, depth - 1)

def koch_snowflake(width=100, depth=1):
    for _ in range(3):
        koch_line(width, depth)
        turtle.right(180 - 60)

if __name__ == "__main__":
    # move fast
    turtle.speed('fastest')

    turtle.penup()
    turtle.goto(-350, 250)
    turtle.pendown()
    koch_snowflake(800, 2)

    # display drawing
    turtle.done()
