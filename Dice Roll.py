def set_number_of_dice():
    number_of_dice = input('Enter how many dice you\'d like to roll: ')
    try:
        int(number_of_dice)

    except ValueError:
        valid_number = False
        while not valid_number:
            number_of_dice = input('Please enter an integer from 1 to 100')
            try:
                int(number_of_dice)
                valid_number = True
            except ValueError:
                continue
    print(number_of_dice)
    print(type(number_of_dice))
    return number_of_dice


set_number_of_dice()
