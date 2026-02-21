import random;

print('''Winning rules of the game ROCK PAPER SCISSORS are : \n'''
      +"if (Rock vs paper) then paper wins \n"
      +"if (Rock vs scissors) then Rock wins \n"
      +"if (Rocscissors vs paper) then scissors wins \n")

while True :
    print("Enter your choice \n" 
                            +"1. is for Rock \n"
                            +"2. is for Paper \n"
                            +"3 is for Scissors \n")
    choice = int(input("enter your choice :"))

    while choice>3 or choice<1 :
        print("enter valid input")

    #user's choice
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    elif choice == 3:
        choice_name = "Scissors"

    print("user's choice is ",choice_name)
    print("\n now its computer's turn ")


    computer_choice = random.randint(1,3)

    #computers choice
    if computer_choice == 1:
        comp_choice_name = "Rock"
    elif computer_choice == 2:
        comp_choice_name = "Paper"
    elif computer_choice == 3:
        comp_choice_name = "Scissors"

    print("computers choice is :",comp_choice_name)

    print(choice_name,"vs",comp_choice_name)


    if choice_name == computer_choice:
        result = "DRAW"
    elif (choice == 1 and computer_choice == 2) or (computer_choice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and computer_choice == 3) or (computer_choice == 1 and choice == 3):
        result = 'Rock'
    elif (choice == 2 and computer_choice == 3) or (computer_choice == 2 and choice == 3):
        result = 'Scissors'

    if result == "draw" :
        print(" == the game is draw ==")
    elif result == choice_name :
        print("  == user wins ==")
    else :
        print("  == compter wins == ")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")