import turtle

def draw_koch_snowflake(t, length, level):
    # Recursively draws one side of a Koch snowflake.

    # :param t: Turtle instance
    # :param length: side length
    # :param level: recursion level
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_snowflake(t, length, level - 1)
        t.left(60)
        draw_koch_snowflake(t, length, level - 1)
        t.right(120)
        draw_koch_snowflake(t, length, level - 1)
        t.left(60)
        draw_koch_snowflake(t, length, level - 1)

def main():
    # User input of recursion level
    level = int(input("Enter the recursion level for the Koch snowflake: "))
    
    # Turtle settings
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Koch's Snowflake")
    
    t = turtle.Turtle()
    # Maximum drawing speed
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Drawing three sides of a snowflake
    for _ in range(3):
        draw_koch_snowflake(t, 400, level)
        t.right(120)

    # Program completion
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
