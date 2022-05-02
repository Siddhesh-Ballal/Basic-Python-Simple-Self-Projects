# Siddhesh Ballal

import random

rock_paper_scissors_dictionary = {1: "Rock", 2: "Paper", 3: "Scissors"}
PlayerScore = 0
ComputerScore = 0 
menuchoice = 1

print("\t\tWelcome to the rock Paper scissors Game!")
while (menuchoice):
    print("\nPlayer's Score: [ ", PlayerScore, " ]")
    print("Computer's Score: [ ", ComputerScore, " ]\n")
    print("\nChoose: ")
    print(" 1) For Rock\n 2) For Paper\n 3) For Scissors\n 4) To Exit\n")
    player_choice = int (input("Please enter the number corresponding to your choice:  "))

    if (player_choice==1 or player_choice==2 or player_choice==3):
        computer_choice = random.randint(1,3)
        print("Alright! I choose: ", rock_paper_scissors_dictionary[computer_choice]) 
    
        if player_choice == 1:
            if computer_choice == 1:
                print("Oh! Looks like it's a Tie!")
            elif computer_choice == 2:
                print("Uh Oh! I win! Better luck next time!")
                ComputerScore += 1
            else:
                print("Bingo! You win!!!")
                PlayerScore += 1 
        
        if player_choice == 2:
            if computer_choice == 1:
                print("Bingo! You win!!!")
                PlayerScore += 1
            elif computer_choice == 2:
                print("Oh! Looks like it's a Tie!")
            else:
                print("Uh Oh! I win! Better luck next time!")
                ComputerScore += 1

        if player_choice == 3:
            if computer_choice == 1:
                print("Uh Oh! I win! Better luck next time!")
                ComputerScore += 1
            elif computer_choice == 2:
                print("Bingo! You win!!!")
                PlayerScore += 1
            else:
                print("Oh! Looks like it's a Tie!")
    
    elif (player_choice==4):
        if PlayerScore > ComputerScore:
            print("You Have Won the Game! You Beat me by: ", PlayerScore - ComputerScore, " points!")
        elif ComputerScore > PlayerScore:
            print("I have Won the Game! I beat You by: ", ComputerScore - PlayerScore, " points!")
        elif PlayerScore == ComputerScore:
            print("Wow! Would you Look at that! We both Scored ", PlayerScore, " points! Looks like a Tie!")
        print("Thank You For Playing With Me! It was A Great Game. Do Visit Again!")
        menuchoice=0
    
    else:
        print("Invalid input. Please enter a number between 1, 2 and 3.")