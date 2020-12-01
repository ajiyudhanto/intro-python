# guessing program

# right_number = 7
# try_counter = 0
# message = 'you lose...'
# while try_counter < 3:
#     input_number = int(input('guess the secret number: '))
#     if input_number == right_number:
#         message = 'you win!'
#         break
#     else:
#         try_counter += 1
# print(message)

# OR
# while try_counter < 3:
#     input_number = int(input('guess the secret number: '))
#     if input_number == right_number:
#         print('you win!')
#         break
#     try_counter += 1
# else:
#     print('you lose...')

# exercise
# temp = 'stop'
# while True:
#     command = input('> ').lower()
#     if command == 'start':
#         if command != temp:
#             print('engine started')
#         else:
#             print('engine was already started')
#     elif command == 'stop':
#         if command != temp:
#             print('engine stopped')
#         else:
#             print('engine was already stopped')
#     elif command == 'exit':
#         break
#     elif command == 'help':
#         print('''
#             asas
#             asasasasas
#             asasasasas
#         ''')
#     else:
#         print('i dont understand what u mean')
#     temp = command

# price = [10, 20, 30]
# for item in price:
#     total = int(input('total: '))
#     print(total * item)

numbers = [5, 2, 5, 2, 2]

# for number in numbers:
#     x_total = ''
#     for multiply in range(number):
#         x_total += 'x'
#     print(x_total)

# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print(largest)

uniques = []
for number in numbers:
    if (number in uniques) == False:
        uniques.append(number)
print(uniques)