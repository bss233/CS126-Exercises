#This is to show how git shows additions


# Function 0: Calculating a Checksum
#
# A checksum is a way to verify that data transmission has occurred without
# data loss or corruption.  This works by taking the data that is about to be
# transmitted and creating some sort of summary value that is dependent on the
# data and then sending it along with the data.  Once the data is received, the
# summary value can be recalculated using the same method and compared to the
# summary value that came with the data: if they match, all is well; if not,
# something went wrong.
#
# Write a function called checksum() that takes in a string and generates a
# simple checksum: add up the numerical codes that correspond to the letters of
# the string and then return this sum
def checksum(aString):
    summation = 0
    for char in aString:
        summation += ord(char)
    return summation



# Function 1: Finding Letter Frequency
#
# Write a function called letter_frequency() that takes in two strings, a word
# and a single letter.  Your function should report what proportion of the
# given word the given letter makes up.  The function should report the
# proportion as a percentage rounded to two decimal places
def letter_frequency(aString, aLetter):
    aLetter = aLetter.lower()
    aString = aString.lower()
    length = len(aString)
    occurences = 0
    for char in aString:
        if char == aLetter:
            occurences += 1
    ratio = occurences / length
    return round(ratio * 100, 2) 



# Function 2: Finding the First Factor
#
# Write a function called first_factor() which takes in a number and returns
# the first number greater than one which evenly divides that number
def first_factor(num):
    counter = 2
    while num % counter != 0:
        counter += 1
    return counter



# Function 3: Detecting Primes
#
# Write a function called is_prime() that takes in an integer and returns True if it is prime and False otherwise.
#
# Hint: remind yourself of what it means for a number to be prime by looking
# it up
#
# Hint: *DON'T* look up how to decide if a number is prime on the
# internet, you will almost certainly find a bunch of really complicated
# code that is overkill for this problem
#
# Hint: You have already implemented another function that you could call to
# make this problem easier (assuming you are doing these in order)
def is_prime(num):
    return first_factor(num) == num


# Function 4: Matching Parentheses
#
# Define a function called all_parens_matched() that takes in a string and
# returns True if the string contains properly matched parenthesis pairs.
#
# Ex.  "(this (string) is) (fine)"
# Ex.  ")this (string) was (doomed from (the start))"
# Ex.  "(this (string looks (fine until the end)))("
#
# Hint: Order matters! You can't simply count the number of open parentheses
# and compare to the number of close parentheses
#
# Hint: Talk this one out (or write out the logic on paper) and then figure
# out how to do it with code. E.G. "Once I've seen an open paren, I need to
# see a closing one to be happy, but if I see more closing parens than open
# ones... etc.
#
# Hint: This problem is hard!

# Removed code to add to a different file
