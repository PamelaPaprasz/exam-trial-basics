pirates = [
    {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
    {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
    {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
    {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
    {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]


def listed_pirates(pirate):
    
    wood_legged_and_more_then_15_gold= []
    
    for i in pirate:
        if i['has_wooden_leg'] == True and i['gold'] > 15:
            wood_legged_and_more_then_15_gold.append(i['Name'])
            
    return wood_legged_and_more_then_15_gold
    
print(listed_pirates(pirates))
    

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that
# - have wooden leg and
# - have more than 15 gold
