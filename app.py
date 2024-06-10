from teams.helpers import (get_exp_count, get_avg_height,
                           list_names, sort_height)
from teams.state import all_teams, teams_stats
from teams.constants import TEAMS 
from time import sleep

def all_team_stats(list):
    for team in list:
        print(f"Team Name : {team['Team Name']}\nExperienced : {team['Experienced']} Players\nInexperienced : {team['Inexperienced']} Players\nAverage Height : {team['Average Height']}\n")



def display_stats(team_name, team):
    experienced, inexperienced = get_exp_count(team)
    
    print(f"###### {team_name} ######\n\n")
    print(f"Total Players: {len(team)}\nNumber Experienced: {experienced}\nNumber Inexperienced: {inexperienced}\nAverage Height: {get_avg_height(team)}\n\n")
    print(f"_-_- Players: From Tallest -_-_\n{list_names(team, "name")}\n\n")
    print(f"_-_- Guardians -_-_\n{list_names(team, "guardians")}")


def welcome():
     print("_____________________\n")
     print("Basketball Team Stats")
     print("_____________________\n")


def menu():
    choice_check = True
    while choice_check:
        print("A: Display Team Stats\nB: View all Team Stats\nC: Quit\n\n")
        user_choice = input("Enter an option:  ")
        
        if user_choice.upper() == "A":
            select_team()
            choice_check = False
        elif user_choice.upper() == "B":
            all_team_stats(teams_stats)
            choice_check = False
        elif user_choice.upper() == "C":
            quit()
        else:
            print("You entered an invalid choice.\n")


def select_team():
    print("_____________________\n")
    print("       Teams         ")
    print("_____________________\n")
    choice_check = True
    while choice_check:
        print("Select which team to view")
        print("1: Panthers\n2: Bandits\n3: Warriors\n")
        user_choice = input("Enter an option:  ")
        if user_choice in ["1", "2", "3"]:
            user_choice = int(user_choice) - 1
            display_stats(TEAMS[user_choice], sort_height(all_teams[user_choice]))
            choice_check = False
        else:
            print("You entered an invalid choice. Choose 1, 2, or 3 for its corresponding team\n")


def continue_menu():
    sleep(1.5)
    input("\nPress 'Enter' to continue.")
    run_app()


def run_app():
    menu()
    continue_menu()
    


if __name__ == "__main__":
    welcome()
    run_app()