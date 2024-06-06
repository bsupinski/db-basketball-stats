


def welcome():
     print("_____________________\n")
     print("Basketball Team Stats")
     print("_____________________\n")


def menu():
    choice_check = True
    while choice_check:
        print("A: Display Team Stats\nB: Quit\n\n")
        user_choice = input("Enter an option:  ")
        
        if user_choice.upper() == "A":
            print("Teams displayed")
            choice_check = False
        elif user_choice.upper() == "B":
            quit()
        else:
            print("You entered an invalid choice.\n")


def select_team():
    print("_____________________\n")
    print("       Teams         ")
    print("_____________________\n")
    choice_check = True
    while choice_check:
        print("1: Panthers\n2: Bandits\n3: Warriors\n")
        user_choice = input("Enter an option:  ")
        if user_choice == "1" or user_choice.lower() == "panthers":
            choice_check = False
            pass
        elif user_choice == "2" or user_choice.lower() == "bandits":
            choice_check = False
            pass
        elif user_choice == "3" or user_choice.lower() == "warriors":
            choice_check = False
            pass
        else:
            print("You entered an invalid choice.\n")





if __name__ == "__main__":
    select_team()