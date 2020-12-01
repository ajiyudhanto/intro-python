house_price = 1000000000

buyer_credit = input("is buyer's credit good? ")

if buyer_credit == 'yes':
    print(house_price * 10 / 100)
else:
    print(house_price * 20 / 100)