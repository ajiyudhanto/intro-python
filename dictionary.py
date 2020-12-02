# dictionary = object in javascript

number_dictionary = {
    "1": "one",
    "2": "two",
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero'
}

input_number = input('phone: ')

converted_number = ''
for number in input_number:
    converted_number += number_dictionary.get(number, '!')
    converted_number += ' '
print(converted_number)