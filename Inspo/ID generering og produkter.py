import random


products = {"0394QHI": {"name": "T‐Shirt", "value": 150},
"3986GXL": {"name": "Hoodie", "value": 300},
"9115ELL": {"name": "Bukser", "value": 350},
"6518IDQ": {"name": "Kjole", "value": 250},
"0789LFN": {"name": "Hat", "value": 100}}


def ID_make():
    numbers = (int(random.randrange(0,6)for i in range(4)))
    letters = (chr(random.randrange(65,90))for i in range(3))
    ID = numbers + letters
    #products[ID] = new_product
    return ID

#At tilføje produkter

def new_product():
    product = input("What is the products name? \n")
    price = input("What is the products price? \n")

    products[ID_make()] = {"name": product, "value" : price}

new_product()
print(products)


#At generere ID
    