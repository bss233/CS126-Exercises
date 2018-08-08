# Checks an integer to see if it is even or odd
userInput = ''
# If the user inputs something that is not an integer, this loop will continue
# to prompt them until they enter an integer
while type(userInput) != int:
    userInput = input("Please enter an integer: ")
    # If the user input is an integer, it is cast to an int type
    if userInput.isdigit():
        userInput = int(userInput)
    # Allows the user to use negative number; .isdigit doesn't support
    # negative numbers
    elif userInput.startswith('-'):

        if userInput[1:].isdigit():
            userInput = int(userInput)
if userInput % 2 == 0:
    # If the user input divided by 2 has no remainder, it is even
    print("That number is even!")
else:
    print("That number is odd!")
