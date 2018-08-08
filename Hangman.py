import random
wordList = ['apple', 'banana', 'coconut', 'dragonfruit', 'grapefruit', 'kiwi',
            'lemon', 'melon', 'nectarine', 'orange', 'pineapple', 'raspberry',
            'tangerine', 'watermelon']
strikes = 0
answer = wordList[random.randint(0, 13)]
for letter in answer:
    print('')
