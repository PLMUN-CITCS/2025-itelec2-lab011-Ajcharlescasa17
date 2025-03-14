# Prompt the user for their age and membership status
age_str = input("Enter your age: ")
membership_str = input("Are you a member? (Yes/No): ")

try:
    # Convert age to integer and normalize membership input
    age = int(age_str)
    membership = membership_str.strip().lower()

    # Nested if...else statement for access control
    if age >= 18:
        if membership == "yes":
            print("Access granted.")
        else:
            print("Membership required for access.")
    else:
        print("Access denied. Must be at least 18 years old.")

except ValueError:
    print("Invalid age input. Please enter an integer.")