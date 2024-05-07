# Timothy Rutkowski 04/10/2024 timothyRutkowski_lab6-3.py

# This program will accept input from a user, determine whether the input is
# numeric or non-numeric, display the results, and terminate when an empty value
# is entered.

# The Main Function of the program
def main():
    # Loop until a break statement is encountered
    while True:
        # Get input from user
        user_input = input('Enter a number (or press Enter to exit): ')
        # Check if input is empty
        if user_input.strip() == '': 
            # Display a message that the program has ended
            print(f'\nProgram ended.')
            # Exit loop and end program
            break
        # Call numTest function to check input
        is_numeric = numTest(user_input)
        # Display results based on is_numeric value
        if is_numeric:
            print(f"\tYour input, '{user_input}', is numeric.\n")
        else:
            print(f"\tYour input, '{user_input}', is not numeric.\n")
        
# Function to test if an input string is numeric
def numTest(user_input):
    try:
        float(user_input)
        # Return message for numeric input
        return True
    except ValueError:
        # Return message for non-numeric input
        return False 
    
# Call the Main Function
if __name__ == '__main__':
    main()
