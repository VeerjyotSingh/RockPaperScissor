import random
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
choices = [rock,paper,scissors]
user = int(input("Choose your move? 1 for rock 2 for paper 3 for Scissors"))-1
robot = random.randint(0,2)

if user == robot:
    print("user:-")
    print(choices[user])
    print("robot:-")
    print(choices[robot])
    print("Its a draw")
elif user == 0 and robot == 1:
    print("user:-")
    print(choices[user])
    print("robot:-")
    print(choices[robot])
    print("Robot win")
elif user == 1 and robot == 2:
    print("user:-")
    print(choices[user])
    print("robot:-")
    print(choices[robot])
    print("Robot win")
elif user == 2 and robot == 0:
    print("user:-")
    print(choices[user])
    print("robot:-")
    print(choices[robot])
    print("Robot win")
elif user == 1 and robot == 0:
    print("user:-")
    print(choices[user])
    print("robot:-")
    print(choices[robot])
    print("You Won")
elif user == 2 and robot == 1:
    print("user:-")
    print(choices[user])
    print("robot:-")
    print(choices[robot])
    print("You Won")
elif user == 0 and robot == 2:
    print("user:-")
    print(choices[user])
    print("robot:-")
    print(choices[robot])
    print("You Won")
else:
    print("error")