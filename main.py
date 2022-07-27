import random
from tkinter import Y
# import colorama #use this to color the cards





cards = ['Ah', 'As', 'Ac', 'Ad', 'Kh', 'Ks', 'Kc', 'Qd', 'Qh', 'Qs', 'Qc', 'Qd', 'Jh', 'Js', 'Jc', 'Jd', '10h', '10s', '10c', '10d', '9h', '9s', '9c', '9d', ]

south, east, north, west, kitty = [], [], [], [], []

# TODO: make array that counts who is dealer

trump = []



def startup():
    print("User is dealer first")





def deal():
    random.shuffle(cards)

    for n in range(5):
        south.append(cards[n])
        east.append(cards[n+5])
        north.append(cards[n+10])
        west.append(cards[n+15])
    
    for n in range(20,24):
        kitty.append(cards[n])
    
    print("Your cards: ", south)

    print(east, north, west, sep="   ")

   
def bid():
    print("Face up card is: ", kitty[0])
    
    if aiBid(east):
        # TODO implement ai calling suit
        print("Player East says pick it up")
    else: 
        print("Player East passes")
    
    if aiBid(north):
        # TODO implement ai calling suit
        print("Player North says pick it up")
    else: 
        print("Player North passes")
    
    if aiBid(west):
        # TODO implement ai calling suit
        print("Player West says pick it up")
    else: 
        print("Player West passes")
    
    play = input("Would you like to play (y or n): ")

    if play == "n":
        # TODO: implment ai calling suit
        trump = input("Please pick a suit(h, d, c, s): ")
        
        



def aiBid(hand):
    return(False)





startup()
deal()
bid()