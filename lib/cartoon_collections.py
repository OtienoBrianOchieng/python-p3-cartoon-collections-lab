def roll_call_dwarves(dwarves):
    for position, dwarf in enumerate (dwarves, start = 1):
        print (f"{position}. {dwarf}")

def summon_captain_planet(planeteers):
    new_list = [f"{planeteer.title()}!" for planeteer in planeteers]
    return new_list

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(cheeses):
    cheese_types = ["cheddar", "gouda", "camembert"]

    for cheese in cheeses:
        if cheese in cheese_types:
            return cheese
        
    return None



    pass
