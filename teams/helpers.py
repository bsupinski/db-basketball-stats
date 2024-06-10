from operator import itemgetter

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
    return(", ".join(name))


def get_exp_count(list):
    experienced = 0
    inexperienced = 0
    for player in list:
        if player['experience'] == True:
            experienced +=1
        else:
            inexperienced += 1 
    return experienced, inexperienced


def get_avg_height(list):
    total_height = 0
    for player in list:
        total_height += player['height']
    return(round(total_height / len(list), 1))


def sort_height(list):
    return sorted(list, key=itemgetter("height"), reverse = True)