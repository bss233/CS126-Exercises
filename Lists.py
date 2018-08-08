# A simple Dictionary
user_input = 0
roman_numerals = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V'}
while user_input not in (1, 2, 3, 4, 5):
    print("Please enter an integer from 1 to 5")
    user_input = int(input())
print("Your number in roman numerals is " + roman_numerals[user_input])
