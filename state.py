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
    clean_guardians(list)
    return list


def list_names(list, key):
    name = [player[key] for player in list]
    print(", ".join(name))



def get_exp_count(list):
    experienced = 0
    notexperienced = 0
    for player in list:
        if player['experience'] == True:
            experienced +=1
        else:
            notexperienced += 1 
    return experienced, notexperienced



def get_avg_height(list):
    total_height = 0
    for player in list:
        total_height += player['height']
    print(round(total_height / len(list), 1))


def filter_by_exp(list):
    filtered_players = [[], []]
    [filtered_players[0].append(player)  if player['experience'] == True else filtered_players[1].append(player) for player in list]
    return(filtered_players)

def create_teams(list):
    teams =[[], [], []]
    for player in list[0]:
        if len(teams[0]) < len(teams[1]):
            teams[0].append(player)
        elif len(teams[1]) < len(teams[2]):
            teams[1].append(player)
        else:
            teams[2].append(player)
    print(len(teams[0]), len(teams[1]), len(teams[2]))

clean_player_list = clean_list(copy.deepcopy(PLAYERS))



if __name__ == "__main__":
    create_teams(filter_by_exp(clean_player_list))
    pass
        