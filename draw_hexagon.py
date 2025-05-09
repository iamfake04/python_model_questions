import turtle

def draw_hexagon(t, side_length):
    for _ in range(6):
        t.forward(side_length)
        t.right(60)

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Hexagon Drawing")
    
    # Create a turtle object
    hexagon_turtle = turtle.Turtle()
    hexagon_turtle.speed(1)  # Set the speed of the turtle
    
    # Draw the hexagon
    draw_hexagon(hexagon_turtle, 100)
    
    # Hide the turtle and display the window
    hexagon_turtle.hideturtle()
    screen.mainloop()

# Example usage
main()