# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)
# Code starts here

#Can you find how many deliveries were faced by batsman  `SC Ganguly`.
deliveries_1st_Inning=(data['innings'][0]['1st innings']['deliveries'])
deliveries_2nd_Inning=(data['innings'][1]['2nd innings']['deliveries'])

def Num_of_deliveries_played(player):
    count_delivery = 0
    for delivery in deliveries_1st_Inning :
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == player:
                count_delivery +=1
    return(count_delivery)
count_deliveries_Ganguly = Num_of_deliveries_played('SC Ganguly')
print(count_deliveries_Ganguly)
#  Who was man of the match and how many runs did he scored ?
Man_of_Match=data['info']['player_of_match'][0]
print(Man_of_Match)
count_runs=0
for delivery in deliveries_1st_Inning :
    for delivery_number, delivery_info in delivery.items():
        if (delivery_info['batsman'] == Man_of_Match):
                count_runs += delivery_info['runs']['batsman']
print(count_runs)
#  Which batsman played in the first inning?
batsman_played = []
for delivery in deliveries_1st_Inning :
    for delivery_number, delivery_info in delivery.items():
        player = delivery_info['batsman']
        if player in batsman_played:
            pass
        else:
            batsman_played.append(player)
print(batsman_played)
# Which batsman had the most no. of sixes in first inning ?
batsman_played_6 = []
for delivery in deliveries_1st_Inning :
    for delivery_number, delivery_info in delivery.items():
        if delivery_info['runs']['batsman'] == 6 :
            batsman_played_6.append(delivery_info['batsman'])
Sixs_dict = Counter(batsman_played_6)
print(max(Sixs_dict, key = Sixs_dict.get))
# Find the names of all players that got bowled out in the second innings.
Batsman_Bolwed_Out_2nd = []
for delivery in deliveries_2nd_Inning :
    for delivery_number, delivery_info in delivery.items():
        if('wicket' in delivery_info) and (delivery_info['wicket']['kind'] == 'bowled'):
            Batsman_Bolwed_Out_2nd.append(delivery_info['wicket']['player_out'])
print(Batsman_Bolwed_Out_2nd)
# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
extras_1st_Inning = (len([delivery_info for delivery in deliveries_1st_Inning
                            for delivery_number, delivery_info in delivery.items()
                            if 'extras' in delivery_info]))
print(extras_1st_Inning)
extras_2nd_Inning = (len([delivery_info for delivery in deliveries_2nd_Inning
                            for delivery_number, delivery_info in delivery.items()
                            if 'extras' in delivery_info]))
print(extras_2nd_Inning)
compare_extras = (extras_2nd_Inning - extras_1st_Inning)
print(compare_extras)
# Code ends here


