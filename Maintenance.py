#Classes

class Stats:
    def __init__(self, buckalous = 10, health = 1, cleanliness = 2, happiness = 1):
        self.buckalous = buckalous
        self.health = health
        self.cleanliness = cleanliness
        self.happiness = happiness
#Spilleren starter med at have 2 health bars, 2 happiness bars og 3 cleanliness, da jeg regner med at man køber dem rene.

class Food:
    def __init__(self, price):
        self.price = price



#Dictionaries

fridge = {
    ":pizza:": 2,
    ":sushi:": 1
}
#Spilleren starter med at have 2 pizzaer.

state = {
    "stage": 0,
    "current_page": 0,
    "user": None
}
#Kan også blive lavet om til en class, jeg har valgt disctionary for diversitet. 
#Page nummer 0 er så home page, dog starter man med at købe et dyr i shop, derfor starter den på x. Husk at ændre det.

