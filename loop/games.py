#scissor , paper , rock game 
import random 

choices = ['scissor', 'paper', 'rock']

for i in range(5):
    user_choice = input('enter your choice(scissor,paper,rock): ')
    computer_choice = random.choice(choices)
    print("computer choice;", computer_choice)

    if user_choice == computer_choice :
        print("tie")

    elif user_choice == 'scissor' and computer_choice == 'paper':
        print('you win ')

    elif user_choice == "rock" and computer_choice == 'scissor':
        print('you win')

    elif user_choice == "paper" and computer_choice == 'rock':
        print("you win ")

    else :
        print("you lose")


    
    
