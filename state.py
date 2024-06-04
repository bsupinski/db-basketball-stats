from constants import TEAMS, PLAYERS
import copy




def clean_height(list):
    for player in list:
        player['height'] = int(player['height'].split(" ")[0])
    return list
        
    

def clean_experience(list):
    for player in list:
        if player['experience'] == "YES":
            player['experience'] = True
        else:
            player['experience'] = False
    return list


def clean_guardians(list):
    for player in list:
        player['guardians'] = player['guardians'].replace(" and", ",")
    return list


def clean_list(list):
    clean_height(list)
    clean_experience(list)
    return list

clean_player_list = clean_guardians(copy.deepcopy(PLAYERS))



if __name__ == "__main__":
    for player in clean_player_list:
        print((player["guardians"]))