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


def team_guardians(list):
    guardians = []
    for player in list:
        guardians.append(player['guardians'])
    print(", ".join(guardians))





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




clean_player_list = clean_list(copy.deepcopy(PLAYERS))



if __name__ == "__main__":
    get_avg_height(clean_player_list)
    pass
        