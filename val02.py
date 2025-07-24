# Input Validation Example 2 -- Basic Input Validation by Hand
# SKE Tutorial Camp 2025
# Department of Computer Engineering, Kasetsart University
# Author: Chawanat Nakasan, D.Eng.
# Download this code from: https://github.com/LunaticNeko/ske-tutorial-camp-2025
# MIT License - https://opensource.org/license/mit/

# (Meta) DIRECTIONS:
# Write a program that calcualtes the size of a rectangle.
# The program must ask the user to input the width and height of the rectangle.
# Then, the program must calculate the size of the rectangle and print it.

# (Task) DIRECTIONS:
# - Make the program output an error message if the user inputs a negative number.
# - When an error occurs, the program should exit immediately.

# EXAMPLE INPUT 1:
# Width: 5
# Height: 10

# EXAMPLE OUTPUT 1:
# Size = 50

# EXAMPLE INPUT 2:
# Width: -5
# Height: 10

# EXAMPLE OUTPUT 2:
# Error: Width cannot be negative.

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

    if width < 0:
        print("Error: Width cannot be negative.")
        return

    if height < 0:
        print("Error: Height cannot be negative.")
        return
        

    # Calculate the size of the rectangle
    size = calculate_rectangle(width, height)

    # Print the result
    print(f"Size = {size}")

# This makes the program run the main function when executed
if __name__ == "__main__":
    main()
