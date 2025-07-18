a=int(input("Enter a number: "))  # Prompt user for input
match a:
    case 1:
        print("You entered one.")
    case 2:
        print("You entered two.")
    case _:
        print("You entered something else.")
        
        
        
# This code snippet demonstrates the use of match-case statements in Python.
# It prompts the user to enter a number and matches it against specific cases.
# If the input matches case 1 or case 2, it prints a corresponding message.
# If the input does not match any specified case, it defaults to the last case using `_`.   