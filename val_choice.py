# Choice Validation Example (Validate choice from list of strings)
# SKE Tutorial Camp 2025
# Department of Computer Engineering, Kasetsart University
# Author: Chawanat Nakasan, D.Eng.
# Download this code from: https://github.com/LunaticNeko/ske-tutorial-camp-2025
# MIT License - https://opensource.org/license/mit/

def main():
    """This program demonstrates how to validate a choice from a list of strings."""

    choices = ["tea", "coffee"]

    user_selection = input(f"Would you like {choices[0]} or {choices[1]}?")

    # Validate the user's choice
    if user_selection in choices:
        print(f"You chose {user_selection}.")
    else:
        print(f"We don't have {user_selection}. Please choose either {choices[0]} or {choices[1]}.")


# This makes the program run the main function when executed
if __name__ == "__main__":
    main()
