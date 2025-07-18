age=int(input("Enter your age: "))  # Prompt user for age input
if age > 18:  # Check if the user is an adult
    print("You are an adult.")
elif age == 18:  # Check if the user is exactly 18
    print("You are exactly 18 years old.")
    
else:  # If the user is not an adult
    print("You are not an adult.")