# house_price = 1000000000

# buyer_credit = input("is buyer's credit good? ")

# if buyer_credit == 'yes':
#     print(house_price * 10 / 100)
# else:
#     print(house_price * 20 / 100)

# is_beautiful = True
# is_kind = False

# if is_beautiful and not is_kind:
#     print('say hello')
# else:
#     print ('ignore')



# exercise
weight = input('Weight: ')
type = input('(L)bs or (K)g: ')

if type.lower() == 'l':
    print(f"You are { float(weight) / 2.2 } kilos")
elif type.lower() == 'k':
    print(f"You are { float(weight) * 2.2 } pounds")