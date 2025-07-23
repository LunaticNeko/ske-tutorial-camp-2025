# Input Value Validation Example (Validate at Input)
# SKE Tutorial Camp 2025
# Department of Computer Engineering, Kasetsart University
# Author: Chawanat Nakasan, D.Eng.
# Download this code from: https://github.com/LunaticNeko/ske-tutorial-camp-2025
# MIT License - https://opensource.org/license/mit/

def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI) from weight and height."""
    return weight / (height ** 2)

def main():
    """This program is a minimal example of value validation."""

    weight = int(input("weight (kg): "))
    height = int(input("height (cm): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
        return

# This makes the program run the main function when executed
if __name__ == "__main__":
    main()
