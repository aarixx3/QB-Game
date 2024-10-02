# Aaron Gould
# Final Project
# COP 2500C
# April 12th, 2023

# Pick the best QB for the MFL, UCF Mascot edition!

# **** https://www.ucf.edu/pegasus/mighty-mascots/ source for story lines ****
# Our dictionary and stats of each mascot!
characters = [{"name": "Knightro",
               'passing_yards': 5250,
               'touchdowns': 36},
              {'name': "Citronaut",
               'passing_yards': 4599,
               'touchdowns': 29},
              {'name': "Vincent the Vulture",
               'passing_yards': 4839,
               'touchdowns': 32},
              {'name': "Puff",
               'passing_yards': 4547,
               'touchdowns': 29}]


# Our rating function to analyze each mascots stats and outputs how good of a quarterback they are for the team.
def character_rating(name, passing_yards, touchdowns):
    if passing_yards >= 5000 and touchdowns >= 36:
        print(f"{name} is the best QB for the team!")
    elif passing_yards >= 4800 and touchdowns >= 30:
        print(f"{name} is a top quarterback.")
    elif passing_yards >= 4599 and touchdowns <= 29:
        print(f"{name} is a great quarterback.")
    else:
        print(f"{name} is one of the worst quarterbacks.")

# Menu function
def menu():
    print("Who do you want as QB on your MFL team!")
    print("Hint: Make sure you check each of their stats first!")
    print("1. Citronaut")
    print("2. Vincent the Vulture")
    print("3. Knightro")
    print("4. Puff")
    print("5. Custom Character")
    print("6. Exit")
    option = int(input("Who do you chose?\n"))
    return option

# Main function
def main():
    print("Welcome to the Mascot Football League!")
    # Beginning loop of main function, looping the menu
    while True:
        option = menu()
        # If option 1, selects "Citronaut"
        if option == 1:
            print("You opted for Citronaut!")
            # Allows user to view Citronaut's stats
            print("1. Stats")
            # Tells the user a little background story of Citronaut
            print("2. Story")
            # User selects this character as starting QB
            print("3. Select this character")
            choice = int(input("Which choice?\n"))
            # Loops choice menu
            if choice == 1:
                # Prints the stats
                print(characters[1])
            elif choice == 2:
                # Story time
                print("Citronaut is an orange shaped astronaut who was the first mascot of"
                      " Florida Technological University (FTU), which later was called University of Central Florida.")
                print("With much disapproval, the character was petitioned by students after one year.")
            elif choice == 3:
                print("Citronaut was selected as your character.")
                # Runs the rating function to see how Citronaut will perform
                return character_rating("Citronaut",4599,29)
            # Else brings you back to the menu
            else:
                print("Invalid Response, back to menu")
                menu()
        # If option 2, selects "Vincent the Vulture"
        elif option == 2:
            print("You opted for Vincent the Vulture!")
            print("1. Stats")
            print("2. Story")
            print("3. Select this character")
            choice = int(input("Which choice?\n"))
            # Loops choices,  Prints the stats
            if choice == 1:
                return characters[2]
            # Prints story
            elif choice == 2:
                print("Vincent the Vulture was chosen as the second mascot because of the presence of vultures"
                      "at the campus.")
                print("The Citronaut/Vincent the Vulture conflict lasted more than a year.")
                print("With the athletics department needing a nickname, they moved on with the vulture idea.")
            # Runs the rating function to see how Vincent the Vulture will perform
            elif choice == 3:
                print("Vincent the Vulture was selected as your character.")
                return character_rating("Vincent the Vulture", 4839, 32)
            # Else brings you back to the menu
            else:
                print("Invalid Response, back to menu")
                menu()
        # If option 3, selects "Knightro"
        elif option == 3:
            print("You opted for Knightro!")
            print("1. Stats")
            print("2. Story")
            print("3. Select this character")
            choice = int(input("Which choice?\n"))
            # Loops choices,  Prints the stats
            if choice == 1:
                print(characters[0])
            # Prints story
            elif choice == 2:
                print(
                    "With the newly acquired Knights nickname, the school went through many iterations of knight"
                    "characters.")
                print("In 1994, a student of the cheerleading team and SGA, created the suit and was dubbed Knightro.")
                print("Charge on!")
            # Selects the character and runs the function to determine performance.
            elif choice == 3:
                print("Knightro was selected as your character.")
                return character_rating("Knightro", 5250, 36)
            # Else brings you back to the menu
            else:
                print("Invalid Response, back to menu")
        # If option 4, selects "Puff"
        elif option == 4:
            print("You opted for Puff!")
            print("1. Stats")
            print("2. Story")
            print("3. Select this character")
            choice = int(input("Which choice?\n"))
            # Loops choices,  Prints the stats
            if choice == 1:
                print(characters[3])
            # Prints story
            elif choice == 2:
                print("Puff was a dragon themed mascot, donated by Disney, who appeared alongside Mack the Knight")
                print("Was only a prelude to the great knight.")
            # Selects the character and runs the function to determine performance.
            elif choice == 3:
                print("Puff was selected as your character.")
                return character_rating("Puff", 4548, 29)
            # Else brings you back to the menu
            else:
                print("Invalid Response, back to menu")
        # Creating a new mascot to store in dictionary
        elif option == 5:
            # Adds their name
            add = input("What is your mascots name?\n")
            # Adds their stats
            passing_yards = int(input("How many passing yards did they have last year?\n"))
            touchdowns = int(input("How many touchdowns did they have last year?\n"))
            # Selects character and runs the function to determine performance
            return character_rating(add,passing_yards,touchdowns)
        # Exits program
        else:
            if option == 6:
                print("Goodbye")
                break
# Call function to run program
main()
