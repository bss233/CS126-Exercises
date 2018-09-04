# Checks an integer to see if it is even or odd
user_input = ''
# If the user inputs something that is not an integer, this loop will continue
# to prompt them until they enter an integer
while type(user_input) != int:
    user_input = input("Please enter an integer: ")
    # If the user input is an integer, it is cast to an int type
    if user_input.isdigit():
        user_input = int(user_input)
    # Allows the user to use negative number; .isdigit doesn't support
    # negative numbers
    elif user_input.startswith('-'):

        if user_input[1:].isdigit():
            user_input = int(user_input)
if user_input % 2 == 0:
    # If the user input divided by 2 has no remainder, it is even
    print("That number is even!")
else:
    print("That number is odd!")
