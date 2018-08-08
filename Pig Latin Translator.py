# A simple English to Pig Latin Translator
word_to_translate = input("Please enter a word to translate: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
tempWord = ''
length = len(word_to_translate)
counter = 0
translated_word = word_to_translate
if word_to_translate[0] in vowels:
    translated_word += 'yay'
else:
    for letter in word_to_translate:
        if letter not in vowels:
            counter += 1
            tempWord += letter
            translated_word = word_to_translate[counter:length]
        else:
            translated_word = (translated_word + tempWord + 'ay').lower()
            break
print(translated_word.capitalize())
