#Classes

class Health:
    def __init__(self, hungry, clean, happy):
        self.hungry = hungry
        self.clean = clean
        self.happy = happy


class Food:
    def __init__(self, number, price):
        self.number = number
        self.price = price

#Dictionaries

def new_stats():
    fridge = {
        "🍕": Food(2, 3),
        "🍓": Food(0, 1),
        "🍩": Food(0, 2),
        "🍙": Food(0, 4)
    }

    state = {
        #"current_page": 0,
        "user": None,
        "stats": Health(0, 0, 0),
        "buckaloues": 10,
        "stage": 0
    }

    return (fridge, state)

users = {}

# (fridge, state) = Maintenance.users[user]   #at få fat i begge states
# state["stage"] = 2 #opdatere stage
# state["stats"].clean += 1  #opdatere stat

#Lists

helpMes = [
    "This game allows you to take care of your pet by playing, feeding and cleaning it", 
    
    "THE CURRENCY",

    "The currency in this game is called *buckaloue* which allows you to shop for items.",
    "You can obtain buckaloues by caring for your pet",

    "COMMANDS",

    "The prefix is >",
    "*>help* for explaining the game. ",
    "*>play* for playing mini games with your pet", 
    "*>feed* for feeding your pet",
    "*>shower* for cleaning your pet", 
    "*>shop* for shopping items for your pet",
    "*>menu* to return back to the menu screen"

    "REACTIONS",

    "You will be able to react on a message using emojis.",
    "Tip:  You can react on a message when the reactions are visible, otherwise you'll write the command/answer (remember the prefix >)",

    "STATS",

    "The stats are the 3 top bars that show you your pets *Hunger, Happiness and Cleanliness*",
    "Keep an eye on your pets stats so that your pet doesn't get sick."

]