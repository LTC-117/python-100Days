import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

if isinstance(user_input, str) and user_input not in ['0', '1', '2']:
    print("You typed an invalid value, you lose!")
    sys.exit(0)

user_choice = int(user_input)

print(options[user_choice])

computer_choice = random.randint(0, 2)

print(f"Computer chose:\n{options[computer_choice]}")

if user_choice == computer_choice:
    print("It's a Draw!!")
elif user_choice - computer_choice not in [1, -2]:
    print("You lose!!")
else:
    print("You win!!!")

# The only possibilities of winning are:
#       Scissors - Paper -> (2 - 1) = 1;
#       Paper - Rock -> (1 - 0) = 1;
#       Rock - Scissors -> (0 - 2) = -2.
# Therefore -> 1, 1, and -2
