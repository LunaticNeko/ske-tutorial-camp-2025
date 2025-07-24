# Input Validation Example 5 -- Input Validation with Membership Testing
# SKE Tutorial Camp 2025
# Department of Computer Engineering, Kasetsart University
# Author: Chawanat Nakasan, D.Eng.
# Download this code from: https://github.com/LunaticNeko/ske-tutorial-camp-2025
# MIT License - https://opensource.org/license/mit/

# (Meta) DIRECTIONS:
# Write a program that calcualtes the size of a shape.
# The program must ask the user to input the dimensions of the shape.
# Then, the program must calculate the size of the shape and print it.

# (Task) DIRECTIONS:
# - Expand the program to also accept other shapes like circles and triangles.
# - The program must first ask the user to type the shape they want to calculate.
# - If the user inputs an invalid shape, the program should loop back and ask again.
# - For circles, ask for the radius; for triangles, ask for the base and height.

# EXAMPLE INPUT 1:
# Shape: rectangle
# Width: 5
# Height: 10

# EXAMPLE OUTPUT 1:
# Size = 50

# EXAMPLE INPUT 2:
# Shape: circle
# Radius: 7

# EXAMPLE OUTPUT 2:
# Size = 153.938

# WARNING: Current code is a copy of val01.py.
# It will be fixed as the lecture progresses.

def calculate_rectangle(width, height):
    """Calculate size of rectangle from width and height."""

    if width < 0:
        raise ValueError("Error: Width cannot be negative.")

    if height < 0:
        raise ValueError("Error: Height cannot be negative.")

    return width * height

def rectangle_menu():
    while True:
        # Get user input for width and height
        try:
            width = int(input("Width: "))
            height = int(input("Height: "))
        except ValueError as e: # expecting ValueError for int function
            print("Input parsing error in width or height. Try again.")
            continue
        try:
            # Calculate the size of the rectangle
            size = calculate_rectangle(width, height)
            break
        except ValueError as e:
            print(e)
    return size

def calculate_circle(radius):
    """Calculate size of circle from radius."""

    if radius < 0:
        raise ValueError("Error: Radius cannot be negative.")

    return (22/7) * (radius ** 2)

def circle_menu():
    while True:
        # Get user input for radius and height
        try:
            radius = int(input("Radius: "))
        except ValueError as e: # expecting ValueError for int function
            print("Input parsing error in radius. Try again.")
            continue
        try:
            # Calculate the size of the rectangle
            size = calculate_circle(radius)
            break
        except ValueError as e:
            print(e)
    return size

# TODO: add support for triangle

def main():
    """Main function to execute the rectangle size calculation program."""

    valid_shapes = ["rectangle", "circle", "triangle"]

    while True:
        # Get the shape from the user
        user_shape = input("Shape [" + ", ".join(valid_shapes) + "]")
        if user_shape not in valid_shapes:
            print("Please type a valid choice.")
            continue
        break

    if user_shape == "rectangle":
        size = rectangle_menu()
    elif user_shape == "circle":
        size = circle_menu()
    # TODO: add support for triangle
    

    # Print the result
    print(f"Size = {size}")

# This makes the program run the main function when executed
if __name__ == "__main__":
    main()
