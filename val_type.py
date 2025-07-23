# Type Validation Example (Validate Type in Function)
# SKE Tutorial Camp 2025
# Department of Computer Engineering, Kasetsart University
# Author: Chawanat Nakasan, D.Eng.
# Download this code from: https://github.com/LunaticNeko/ske-tutorial-camp-2025
# MIT License - https://opensource.org/license/mit/

def calculate_bmi(weight: int, height: int) -> float:
    """Calculate Body Mass Index (BMI) from weight and height."""

    # raise error if not integer
    if not isinstance(weight, int):
        raise TypeError("Weight must be an integer.")

    if not isinstance(height, int):
        raise TypeError("Height must be an integer.")

    return weight / (height ** 2)

def main():
    """This program is a minimal example of value validation."""

    weight = int(input("weight (kg): "))
    height = int(input("height (cm): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
        return
    
    try:
        bmi = calculate_bmi(weight, height / 100)  # Convert height to meters
        print(f"Your BMI is: {bmi:.2f}")
    except TypeError as e:
        print(f"Error: {e}")

# This makes the program run the main function when executed
if __name__ == "__main__":
    main()
