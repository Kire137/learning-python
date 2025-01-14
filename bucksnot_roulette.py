from numpy import random
from time import sleep

# track shells
next_round = ""
sequence = []

round_number = 1

# health
your_health = 4
dealer_health = 4

# track items and what they do
items_list=["beer","cigarettes","saw","handcuffs","magnifying glass"]
effects=["rack","heal","damage","skip","next"]
your_items=[]
dealer_items=[]

# when called, give an amount (items_amount) of random items, and return them as an array
def give_items(items_amount):    
    global your_items
    global dealer_items
    for i in range(items_amount):
        your_items.append(items_list[random.randint(len(items_list))])
        dealer_items.append(items_list[random.randint(len(items_list))])

# see how many rounds will be in the gun, and how many will be live. Return an array [(live),(total)]
def load_gun(round_number):
    return([((random.randint(2 * round_number) + 1)),(((2 * round_number) + random.randint(3) + 1))])

# call when a use uses an item, return the effect that is being applied and a bit of flavor text.
def use_item():
    global your_items
    global next_round
    global your_health
    global sequence
    item = input("Which item do you want to use? ")
    if item == "beer":
        try:
            your_items.remove("beer")
        except:
            print("You don't have a beer.")
        else:
            print("You drink the beer...a ", " round is racked.", sep=next_round)
            sequence.pop[0]
            next_round = sequence[0]
            your_turn()
    elif item == "cigarettes":
        try:
            your_items.remove("cigarettes")
        except:
             print("You don't have a pack of cigarettes.")
        else:
            print("You pull out a cigarette and smoke it in one long draw. One health restored.")
            your_health += 1
            your_turn()
    elif item == "saw":
        try:
            your_items.remove("saw")
            print("In one fluid motion, the saw tears through the end of the shotgun. It will deal double damage next shot.")
            #return("damage")
        except:
             print("You don't have a saw.")
    elif item == "handcuffs":
        try:
            your_items.remove("handcuffs")
            print("The handcuffs click into place around the dealer's hands. Their next turn is skipped.")
            #return("skip")
        except:
             print("You don't have any handcuffs.")
    elif item == "magnifying glass":
        try:
            your_items.remove("magnifying glass")
            print("Inspecting the gun, you see that the next round is ", ".", sep=next_round)
            your_turn()
        except:
             print("You don't have a magnifying glass.")
    else:
        print("That wasn't an item name.")

# Choices to make on your turn
def your_turn():
    global next_round
    next_round = sequence[0]
    print("Your turn.")
    choice = input("Will you FIRE or use an ITEM? ")
    if choice == "FIRE":
        who = input("Shoot MYSELF or the DEALER? ")
        if who == "MYSELF":
            next_turn(fire("shoot_you"))
        elif who == "DEALER":
            next_turn(fire("shoot_dealer"))
    elif choice == "ITEM":
        use_item()
    else:
        print("choice not valid")

# Runs when you actually fire
def fire(shoot_who):
    global sequence
    print("The trigger slowly pulls back and...")
    if next_round == "blank":
        sleep(1)
        print("Click.")
        if shoot_who == "shoot_you":
            sequence.pop[0]
            return("your_turn")
        else:
            sequence.pop[0]
            return("dealer_turn")
    elif next_round == "live" and shoot_who == "shoot_dealer":
        sequence.pop[0]
        print("A massive bang rings through the room. The dealer is knocked back. After a moment, he reappears, even angrier than before.")
        return("dealer_shot")
    elif next_round == "live" and shoot_who == "shoot_you":
        sequence.pop[0]
        print("A flash of light!... Then nothing. The trigger was pulled on a live round, aimed at you.")
        return("you_shot")
    else:
        print("fire no matches bug")

def start_round(round_number):
    global next_round
    global sequence
    shells_loaded = load_gun(round_number)
    print("There are ", shells_loaded[0], " live rounds and ", (shells_loaded[1] - shells_loaded[0]), " blanks.")
    sleep(1)
    for x in range(shells_loaded[0]):
        sequence.append("live")
    for x in range(shells_loaded[1] - shells_loaded[0]):
        sequence.append("blank")
    random.shuffle(sequence)
    next_round = sequence[0]
    give_items(round_number + 1)
    print("You have items", your_items)
    print("Dealer has items", dealer_items)

def next_turn(result):
    global your_health
    global dealer_health
    sleep(1)
    if result == "your_turn":
        your_turn()
    elif result == "dealer_turn":
        dealer_turn()
    elif result == "dealer_shot":
        dealer_health -= 1
        print("Your health: ", your_health)
        print("Dealer health: ", dealer_health)
    elif result == "you_shot":
        your_health -= 1
        print("Your health: ", your_health)
        print("Dealer health: ", dealer_health)
    else:
        print("This is an unobtainable bug. How the actual fuck did you get here?")

def dealer_turn():
    global next_round
    next_round = sequence[0]
    print("It's the dealer's turn.")
    next_turn(fire("shoot_you"))



print("A number of live and blank shells are loaded into the shotgun each round.")
print("Items may change the course of the game.")
print("Words in uppercase are valid commands.")
name = input("The dealer has no liability for injury or death. To confirm the terms, sign here: ")
print("Thank you, \"", ".\" The game may now begin.", sep=name)
sleep(1)
print("")

start_round(round_number)
your_turn()