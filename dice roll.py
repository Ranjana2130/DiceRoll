import random

def roll_dice():
    
    dice_value = random.randint(1, 6)
    return dice_value
while True:
  
    print("Rolling the dice...")
    result = roll_dice()
    print("The dice shows: " ,result)
    
   
    roll_again = input("Do you want to roll the dice again? (yes/no): ").lower()
    if roll_again != 'yes':
        print("Thanks for playing!")
        break
