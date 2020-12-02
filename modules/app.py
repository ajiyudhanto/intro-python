# from utils import find_max

# numbers = [1, 2, 3, 85, 32, 32, 34, 12243, 54, 6567]
# print(find_max(numbers))

import random

class Dice:
    def roll(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        return (dice_1, dice_2)


dice = Dice()
print(dice.roll())