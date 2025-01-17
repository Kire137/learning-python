from numpy import random
from time import sleep
import camelcase

# ok so for real this time
# theres gonna be a variable for everything so that i can just basically make a ton of if statements
# BY DEFAULT, 0 means dealer and 1 means player

dealerHealth = 4 #self-explanitory
yourHealth = 4 #self-explanitory
turn = 1 #who's turn is it?
round = 0 #what round are we on?
aimedAt = None #who is being shot at?
nextShell = None #0 is blank and 1 is live
sequence = [1] #String of all shells
gunSawn = 0 #Whether the gun deals double dagmgame
handcuffed = 0 #Whether to skip the next person's turn
yourItems = [] #What items you have
dealerItems = [] #what items the dealer has
itemsList = ["beer", "cigarettes", "saw", "handcuffs", "magnifying glass"] #all possible items


def game():
    while yourHealth > 0 and dealerHealth > 0:
        while sequence.count(1) > 0:
            loadGun()
            updateNextShell()
            while turn == 1:
                yourTurn()
                endTurn()
            while turn == 0:
                dealerTurn()
                endTurn()
    return
    

def yourTurn():
    global aimedAt
    print("Your turn.")
    while turn == 1:    
        choice = input("Will you FIRE or use an ITEM? ")
        while choice != "FIRE" and choice != "ITEM":
            choice = input("That was not a valid command. Please use FIRE or ITEM. ")
            if choice == "FIRE" or choice == "ITEM":
                break
        if choice == "FIRE":
            who = input("Shoot MYSELF or the DEALER? ")
            while who != "MYSELF" and who != "DEALER":
                who = input("That's not a valid target. Please aim at MYSELF or the DEALER.")
                if who == "MYSELF" or choice == "DEALER":
                    break
            if who == "MYSELF":
                aimedAt = 1
                return
            if who == "DEALER":
                aimedAt = 0
                return
            return
        if choice == "ITEM":
            useItem()

def useItem():
    global yourItems
    global nextShell
    global yourHealth
    global sequence
    global gunSawn
    global handcuffed
    item = input("Which item do you want to use? ")
    while item not in itemList:
        item = input("That's not a valid item. Please say a real item.")
        if item in itemList:
            break
    if item == "beer":
        try:
            yourItems.remove("beer")
        except:
            print("You don't have a beer.")
        else:
            print("You drink the beer...a ", " round is racked.", sep=nextShell)
            sequence.pop[0]
            updateNextShell()
            return
    if item == "cigarettes":
        try:
            yourItems.remove("cigarettes")
        except:
             print("You don't have a pack of cigarettes.")
             return
        else:
            print("You pull out a cigarette and smoke it in one long draw. One health restored.")
            yourHealth += 1
            return
    if item == "saw":
        try:
            yourItems.remove("saw")
        except:
             print("You don't have a saw.")
             return
        else:
            print("In one fluid motion, the saw tears through the end of the shotgun. It will deal double damage next shot.")
            gunSawn = 1
            return
    if item == "handcuffs":
        try:
            yourItems.remove("handcuffs")
        except:
             print("You don't have any handcuffs.")
             return
        else:
            print("The handcuffs click into place around the dealer's hands. Their next turn is skipped.")
            handcuffed = 1
            return
    if item == "magnifying glass":
        try:
            yourItems.remove("magnifying glass")
        except:
             print("You don't have a magnifying glass.")
             return
        else:
            print("Inspecting the gun, you see that the next round is ", ".", sep=nextShell)
            return
    else:
        print("item nope debug")


def dealerTurn():
    aimedAt = 1
    return

def endTurn():
    global turn
    global yourHealth
    global dealerHealth
    global sequence
    updateNextShell()
    if turn == 1:
        if aimedAt == 1:
            if nextShell == 1:
                print("you ouchie")
                if gunSawn == 1:
                    yourHealth -= 2
                else:
                    yourHealth -= 1
                if handcuffed == 1:
                    turn = 1
                else:
                    turn = 0
            if nextShell == 0:
                print("click")
                turn = 1
        if aimedAt == 0:
            if nextShell == 1:
                print("you shoot dealer")
                if gunSawn == 1:
                    dealerHealth -= 2
                else:
                    dealerHealth -= 1
                if handcuffed == 1:
                    turn = 1
                else:
                    turn = 0
            if nextShell == 0:
                print("better luck next time")
                if handcuffed == 1:
                    turn = 1
                else:
                    turn = 0
    if turn == 0:
        if aimedAt == 1:
            if nextShell == 1:
                print("dealer shoot you")
                if gunSawn == 1:
                    yourHealth -= 2
                else:
                    yourHealth -= 1
                if handcuffed == 1:
                    turn = 0
                else:
                    turn = 1
            if nextShell == 0:
                print("dealer misses")
                if handcuffed == 1:
                    turn = 0
                else:
                    turn = 1
        if aimedAt == 0:
            if nextShell == 1:
                print("dealer shoot self")
                if gunSawn == 1:
                    dealerHealth -= 2
                else:
                    dealerHealth -= 1
                if handcuffed == 1:
                    turn = 0
                else:
                    turn = 1
            if nextShell == 0:
                print("dealer fire blank on self")
                turn = 0
    print("now it updates")
    sequence.pop(0)
    updateNextShell()
    resetEffects()


def resetEffects():
    global gunSawn
    global handcuffed
    gunSawn = 0
    handcuffed = 0

def updateNextShell():
    global nextShell
    nextshell = sequence[0]
    return

def gameIntro():
    global round
    print("This is the text that plays when you start the game. Copy paste this from attempt one.")
    round += 1

def loadGun():
    global sequence
    sequenceCalc = [((random.randint(2 * round) + 1)),(((2 * round) + random.randint(3) + 1))]
    for i in range(sequenceCalc[0]):
        sequence.append(1)
    for i in range(sequenceCalc[1] - sequenceCalc[0]):
        sequence.append(0)
    print("There are ", sequenceCalc[0], " live shells and ", (sequenceCalc[1] - sequenceCalc[0]), " blanks.")
    random.shuffle(sequence)
    updateNextShell()
    return

def startGame():
    gameIntro()
    game()





startGame()

#DEBUGGING ////////////////////
#yourTurn()