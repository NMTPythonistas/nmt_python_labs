import turtle

def draw_tree(branch_size, max_branches=5):
    # done drawing?
    if max_branches <= 0:
        return

    turtle.speed("fastest")

    # start drawing
    turtle.pendown()
    turtle.forward(branch_size)
    # do not draw anything else
    turtle.penup()

    # save the current position and direction
    p, h = turtle.position(), turtle.heading()

    # draw the right branch
    turtle.right(45)
    draw_tree(branch_size / 2, max_branches - 1)

    # jump back
    turtle.setposition(p)
    turtle.setheading(h)

    # draw the left branch
    turtle.left(45)
    draw_tree(branch_size / 2, max_branches - 1)

def main():
    # face up
    turtle.left(90)
    draw_tree(200, max_branches=9)
    turtle.done()

if __name__ == "__main__":
    main()
