import random

#first we need to define the function that will roll the dice
def dice_roll():

 roll = input("Ready to roll? :D (y/n) : ")

 while roll.lower() == "Y".lower():
  dice_one = random.randint(1,6)
  dice_two = random.randint(1,6)

  print("Here are your lucky numbers: {} and {}".format(dice_one, dice_two))

  roll = input("Ready to roll again? (y/n) : ")
  
dice_roll()