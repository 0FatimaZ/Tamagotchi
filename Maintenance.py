#Classes

class Health:
    def __init__(self, hunger, cleanliness, happiness):
        self.health = hunger
        self.cleanliness = cleanliness
        self.happiness = happiness


class Food:
    def __init__(self, number, price):
        self.number = number
        self.price = price
        


#Dictionaries

pet = {
    "buckaloues": 10,
    "stats": Health(2, 3, 2)
}

fridge = {
    "🍕": 2,
    "🍓": 0,
    "🍩": 0,
    "🍙": 0,
    "empty": False
}
"""
fridge = {
    "🍕": Food(2, 3),
    "🍓": Food(0, 1),
    "🍩": Food(0, 2),
    "🍙": Food(0, 4),
    "empty": False
}
"""
#spøg maya hvorfor jeg får AtributeError: 'bool' object has no attribute 'number' selv om koden tydeligvis virker. og bare generelt om brugen af classes i dictionaris fordi jeg er ret sikker på stats også er fucked.


state = {
    "stage": 0,
    "current_page": 0,
    "user": None
}
#Page nummer 0 er så home page, dog starter man med at købe et dyr i shop, derfor starter den på x. Husk at ændre det.