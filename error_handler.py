def multiply(number_1, number_2):
    return number_1 * number_2


try:
    number_1 = int(input('number 1: '))
    number_2 = int(input('number 2: '))
    print(multiply(number_1, number_2))
except SyntaxError:
    print('syntax error')
except TypeError:
    print('input must be number')