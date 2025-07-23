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
# - Only when the output is not an integer, round the output to 3 decimal places.

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
    return width * height

def main():
    """Main function to execute the rectangle size calculation program."""
    # Get user input for width and height
    width = int(input("Width: "))
    height = int(input("Height: "))

    # Calculate the size of the rectangle
    size = calculate_rectangle(width, height)

    # Print the result
    print(f"Size = {size}")

# This makes the program run the main function when executed
if __name__ == "__main__":
    main()
