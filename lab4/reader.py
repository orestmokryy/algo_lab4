import re


def get_data(path):
    try:
        with open(path) as file:
            number_sequence = ''
            data = file.read()
            divided = [el for el in data.split()]
            for element in divided:
                index = divided.index(element)
                match = re.fullmatch(r'[01]+', element)
                if match and index != len(divided) - 1:
                    number_sequence = number_sequence + (match.group())
                elif index == len(divided) - 1:
                    if 0 < len(number_sequence) < 100 and 0 < int(element) < 100:
                        return number_sequence, int(element)
                    else:
                        print('Input doesn`t match the condition')
                        return
                else:
                    print('Invalid input')
                    return
    except FileNotFoundError:
        print("File doesn't exist")
        return
    except ValueError:
        print('Wrong data type')
        return
