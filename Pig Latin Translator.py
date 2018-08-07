# A simple English to Pig Latin Translator
wordToTranslate = input("Please enter a word to translate: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
tempWord = ''
length = len(wordToTranslate)
counter = 0
translatedWord = wordToTranslate
if wordToTranslate[0] in vowels:
    translatedWord += 'yay'
else:
    for letter in wordToTranslate:
        if letter not in vowels:
            counter += 1
            tempWord += letter
            translatedWord = wordToTranslate[counter:length]
        else:
            translatedWord = (translatedWord + tempWord + 'ay').lower()
            break
print(translatedWord.capitalize())
