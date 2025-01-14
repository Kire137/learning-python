from numpy import random
from time import sleep

def give_items(items_amount):
    items=["beer","cigs","saw","cuffs","glass"]
    items_given=[]
    for i in range(items_amount):
        items_given.append(items[random.randint(len(items))])
    return items_given

def load_gun(round_number):
    pass
