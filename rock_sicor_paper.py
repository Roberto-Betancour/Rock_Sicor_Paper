import random

computer_choice=random.choice(["rock","scissors","paper"])

#typing error identification
while True:
    user_choice=input("Enter your choice: rock,scissors or paper: ")
    if user_choice=='rock':
        break
    elif user_choice=='scissors':
        break
    elif user_choice=='paper':
        break
    else:
        print('A typing error has occured, please try again')


print("Computers choice is: ",computer_choice)
if computer_choice == user_choice:
    print("TIE")
elif user_choice=="rock" and computer_choice=="scissors":
    print("You WIN")
elif user_choice=="paper" and computer_choice=="rock":
    print("You WIN")
elif user_choice=="scissors" and computer_choice=="paper":
    print("You WIN")
else:
    print("You loss, Computer Wins")
