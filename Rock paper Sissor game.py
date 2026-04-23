import random

# Print game rules
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins\n"
      + "Rock vs Scissors -> Rock wins\n"
      + "Paper vs Scissors -> Scissors wins\n")

while True:

    print("Enter your choice")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    # User input
    choice = int(input("Enter your choice: "))

    # Validate input
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please: "))

    # Convert user choice number to name
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print("User choice is:", choice_name)
    print("Now it's Computer's turn...")

    # Computer random choice
    comp_choice = random.randint(1, 3)

    # Convert computer choice number to name
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, "vs", comp_choice_name)

    # Determine winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = "Paper"
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = "Rock"
    else:
        result = "Scissors"

    # Print result
    if result == "DRAW":
        print("It's a tie!")
    elif result == choice_name:
        print("User wins!")
    else:
        print("Computer wins!")

    # Play again
    ans = input("Do you want to play again? (Y/N): ").lower()
    if ans == 'n':
        break

print("Thanks for playing!")