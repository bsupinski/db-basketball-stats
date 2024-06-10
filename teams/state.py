from teams.constants import TEAMS, PLAYERS
from teams.helpers import clean_list, get_exp_count, get_avg_height
# from constants import TEAMS, PLAYERS
# from helpers import clean_list, get_exp_count, get_avg_height
import copy 

teams_stats = []


def filter_by_exp(list):
    filtered_players = [[], []]
    [filtered_players[0].append(player)  if player['experience'] == True else filtered_players[1].append(player) for player in list]
    return(filtered_players)


def distribute_player(split_list, list):
    for player in list:
        if len(split_list[0]) < len(split_list[1]):
            split_list[0].append(player)
        elif len(split_list[1]) < len(split_list[2]):
            split_list[1].append(player)
        else:
            split_list[2].append(player)
    return split_list


def create_teams(list):
    teams =[[], [], []]
    distribute_player(teams, list[0])
    distribute_player(teams, list[1])
    return teams


def create_team_stats():
    for index, team in enumerate(TEAMS):
        stats = {}
        exp, inexp = get_exp_count(all_teams[index])
        stats['Team Name'] = team
        stats['Experienced'] = exp
        stats['Inexperienced'] = inexp
        stats["Average Height"] = get_avg_height(all_teams[index])
        teams_stats.append(stats)

clean_player_list = clean_list(copy.deepcopy(PLAYERS))
all_teams = create_teams(filter_by_exp(clean_player_list))

create_team_stats()





if __name__ == "__main__":
    
    print(teams_stats)