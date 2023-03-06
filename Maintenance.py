#Classes

class Health:
    def __init__(self, hunger = 0, cleanliness = 0, happiness = 0):
        self.health = hunger
        self.cleanliness = cleanliness
        self.happiness = happiness


class Food:
    def __init__(self, number, price):
        self.number = number
        self.price = price

#Dictionaries

fridge = {
    "🍕": Food(2, 3),
    "🍓": Food(0, 1),
    "🍩": Food(0, 2),
    "🍙": Food(0, 4)
}

def fridge_empty():
    total = 0
    for food in fridge.values():
        total += food.number
    return total == 0

state = {
    "current_page": 0,
    "user": None,
    "stats": Health(0, 0, 0),
    "buckaloues": 10
}

#Lists

helpMes = [
    "This game allows you to take care of your pet by playing, feeding and cleaning it", 
    
    "THE CURRENCY",

    "The currency in this game is called *buckaloue* which allows you to shop for items.",
    "You can obtain buckaloues by caring for your pet",

    "COMMANDS",

    "The preifx is >",
    "*>Help* for explaining the game. ",
    "*>Play for playing mini games with your pet", 
    "*>Feed for feeding your pet",
    "*>Shower for cleaning your pet", 
    ">Shop for shopping items for your pet",

    "REACTIONS",

    "You will be able to react on a message using emojis.",
    "Tip:  You can react on a message when the reactions are visible, otherwise you'll write the command/answer (remember the prefix >)"

    "STATS",

    "The stats are the 3 top bars that show you your pets *Hunger, Happiness and Cleanliness*",
    "Keep an eye on your pets stats so that your pet doesn't get sick."

]