# A simple Dictionary
userInput = 0
romanNumerals = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V'}
while userInput not in (1, 2, 3, 4, 5):
    print("Please enter an integer from 1 to 5")
    userInput = int(input())
print("Your number in roman numerals is " + romanNumerals[userInput])
