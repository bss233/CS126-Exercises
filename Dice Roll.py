import random


def check_not_alpha(input_value):
    try:
        int(input_value)
        return True
    except ValueError:
        return False


def check_range_number_of_dice(input_value):
    if 0 < input_value <= 100:
        return True
    else:
        return False


def check_valid_setup_number_of_dice(input_value):
    if check_not_alpha(input_value):
        if check_range_number_of_dice(int(input_value)):
            return True
    else:
        return False


def check_valid_type_of_dice(input_value):
    valid_types = ['D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    check_type = input_value.strip().upper()
    if check_type in valid_types:
        return True
    else:
        return False


def set_number_of_dice():
    number_of_dice = input('Enter how many dice you\'d like to roll: \n')
    while not check_valid_setup_number_of_dice(number_of_dice):
        number_of_dice = input('Please enter an integer from 1 to 100: \n')
    return int(number_of_dice)


def set_type_of_dice():
    print('Types of dice: D4, D6, D8, D10, D12, D20, D100 (percentile)')
    type_of_dice = input('Enter the type you\'d like to roll; Ex) D6: \n')
    while not check_valid_type_of_dice(type_of_dice):
        print('Valid types: D4, D6, D8, D10, D12, D20, D100')
        type_of_dice = input('Please enter a valid type in the format D6: \n')
    return type_of_dice.upper()


def percentile_roll(number_of_dice):
    results = []
    for iteration in range(number_of_dice):
        current_roll = 10*(random.randint(1, 10))
        results.append(current_roll)
    average_results = (sum(results)/number_of_dice)
    results.append(average_results)
    return results


def roll_dice(dice_type, number_of_dice):
    type_number = int(dice_type[1:])
    results = []
    for iteration in range(number_of_dice):
        current_roll = random.randint(1, type_number)
        results.append(current_roll)
    sum_results = sum(results)
    results.append(sum_results)
    return results


def main():
    type_of_dice = set_type_of_dice()
    number_of_dice = set_number_of_dice()
    if type_of_dice == 'D100':
        roll_results = percentile_roll(number_of_dice)
        roll_sum = roll_results[-1]
        roll_results.pop()
        print('Average: ', roll_sum)
        print('Roll Results: ', roll_results)
    else:
        roll_results = roll_dice(type_of_dice, number_of_dice)
        roll_sum = roll_results[-1]
        roll_results.pop()
        print('Roll Sum: ',  roll_sum)
        print('Roll Results: ', roll_results)


if __name__ == "__main__":
    main()
