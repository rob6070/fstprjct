# 9.12: Dice

# 1. Make a class Die with one attribute called sides, which has a
# default value of 6.
#
# 2. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has.
#
# 3. Make a 6-sided die and roll it 10 times.
#
# 4. Make a 10-sided die and a 20-sided die.
#
# 5. Roll each die 10 times.

print('\ndice.py\n')

from random import randint

class Die:
    '''Create a die'''

    #initialize the attributes
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        '''Create a method that rolls a random number depending
        on the number of sides the die has'''

        for x in range(10):
            print(randint(1, self.sides))

print("\nLet's roll a 6-sided die")
my_die = Die()
my_die.roll_die()

print("\nLet's roll a 10-sided die")
new_roll = my_die.sides = 10
my_die.roll_die()

print("\nLet's roll a 20-sided die")
new_roll = my_die.sides = 20
my_die.roll_die()

















































