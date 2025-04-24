import turtle

def koch_curve(t, order, size):
    """
    Draw a Koch curve using a turtle.
    
    Parameters:
        t (turtle.Turtle): Turtle object to draw with
        order (int): Level of recursion
        size (float): Length of the curve
    """
    if order == 0:
        # Base case: draw a straight line
        t.forward(size)
    else:
        # Recursive case: replace each line with 4 lines
        koch_curve(t, order-1, size/3)   # Draw first segment
        t.left(60)                       # Turn left 60 degrees
        koch_curve(t, order-1, size/3)   # Draw second segment
        t.right(120)                     # Turn right 120 degrees
        koch_curve(t, order-1, size/3)   # Draw third segment
        t.left(60)                       # Turn left 60 degrees
        koch_curve(t, order-1, size/3)   # Draw fourth segment

def koch_snowflake(t, order, size):
    """
    Draw a Koch snowflake using a turtle.
    
    Parameters:
        t (turtle.Turtle): Turtle object to draw with
        order (int): Level of recursion
        size (float): Length of the side of the initial triangle
    """
    # Draw three Koch curves to form a snowflake
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    # Get the level of recursion from the user
    try:
        level = int(input("Введіть рівень рекурсії для сніжинки Коха (рекомендовано 0-5): "))
        if level < 0:
            print("Рівень має бути невід'ємним цілим числом. Використовується рівень 0.")
            level = 0
    except ValueError:
        print("Некоректне введення. Використовується рівень 2 за замовчуванням.")
        level = 2
    
    # Set up the turtle
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Фрактал 'Сніжинка Коха'")
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.penup()
    t.goto(-150, 100)  # Position the turtle
    t.pendown()
    
    # Draw the Koch snowflake
    koch_snowflake(t, level, 300)
    
    # Hide the turtle and display the result
    t.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()
