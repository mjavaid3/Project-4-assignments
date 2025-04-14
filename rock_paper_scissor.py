# Ultimate Battle Arena: Rock vs Paper vs Scissors
import random

# Display game rules with better formatting
print(" Rules of the Game \n"
      "• Rock crushes Scissors\n"
      "• Paper covers Rock\n"
      "• Scissors cut Paper\n")

while True:
    print("\nChoose your weapon:\n"
          "1 - Rock\n"
          "2 - Paper\n"
          "3 - Scissors\n")
    
    # Get player's selection
    player_selection = int(input("Your move warrior: "))
    
    # Validate input
    while player_selection > 3 or player_selection < 1:
        player_selection = int(input("Invalid weapon! Choose 1-3: "))
    
    # Map selection to weapon name
    weapon_names = {1: 'Rock', 2: 'Paper', 3: '✂Scissors'}
    player_weapon = weapon_names[player_selection]
    
    print(f"\nYou chose: {player_weapon}")
    print("The computer is selecting its weapon...")
    
    # Computer's selection (ensuring different choice for more excitement)
    computer_selection = random.randint(1, 3)
    while computer_selection == player_selection:
        computer_selection = random.randint(1, 3)
    
    computer_weapon = weapon_names[computer_selection]
    print(f"Computer chose: {computer_weapon}")
    
    print(f"\n{player_weapon}  VS  {computer_weapon}")
    
    # Determine battle outcome
    if player_selection == computer_selection:
        print("The battle ends in a stalemate!")
    elif ((player_selection == 1 and computer_selection == 3) or
          (player_selection == 3 and computer_selection == 1)):
        print("Rock smashes Scissors! ", end="")
        print("You conquer!") if player_selection == 1 else print("The machine triumphs!")
    elif ((player_selection == 1 and computer_selection == 2) or
          (player_selection == 2 and computer_selection == 1)):
        print("Paper envelops Rock! ", end="")
        print("You dominate!") if player_selection == 2 else print("The AI prevails!")
    else:
        print("Scissors slice Paper! ", end="")
        print("You emerge victorious!") if player_selection == 3 else print("The computer wins!")
    
    # Play again prompt
    rematch = input("\nDo you dare to battle again? (Y/N): ").lower()
    if rematch == 'n':
        break

print("\nThank you for battling in the Arena! Until next time! ")
