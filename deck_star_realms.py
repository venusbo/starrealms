
## track runtime
import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

## Hashmaps and arrays for decks in star realms game

## card attributes

# card_authority_points = {'scout': 1, 'explorer': 2, 'battle blob': 6, 'Battle pod': 2 }
#
# card_combat_points = {'battle blob' : 8, 'battle pod' : 2}
#
#
#
#
# scout = {'scrapping_ability' : False}
#
# explorer = {'scrapping_ability' : True, 'scrapping_dmg': 2}
#
# battle_blob = {'scrapping_ability': True, 'scrapping_dmg': 4}



## returning scrap damage from ship cars
# def scrap_damage(card):
#     if (card['scrapping_ability']) == True:
#         scrap_dmg = (card['scrapping_dmg'])
#         return scrap_dmg
#
#     elif (card['scrapping_ability'] == False):
#         scrap_dmg = 0
#         return scrap_dmg
#
# print(scrap_damage(scout))
# print(scrap_damage(explorer))
#
# print(scrap_damage(battle_blob))


##print(card_authority_points['scout'])
##print(card_scrapping_ability['scout'])
##print(card_scrapping_ability['battle blob'])

## decks

## RESTARTING
## Using objects and classes in python

## setting player's starting hp

player1_hp = int(50)
player2_hp = int(50)

## creating object class: cards

class card:
    def __init__(self, key, name, cost, faction):
        self.key = key ## str
        self.name = name ## str
        self.cost = cost ## int
        self.faction = faction ## str

    ## representing card as str
    def __repr__(self):
        return "{self.key}".format(self=self)

    def get_key(self):
        print(self.key)

    def get_name(self):
        print(self.name)

    def get_cost(self):
        print(self.cost)

    def get_faction(self):
        print(self.faction)

    def is_base_set(self):
        print(self.is_base_card)



## creating card class for card types: ships and bases

class ship(card):
    def __init__(self, key, name, cost, faction, combat, trade, regen): ## 6 values
        super().__init__(key, name, cost, faction)
        self.combat = combat ## int
        self.trade = trade ## int
        self.regen = regen ## int

    def get_combat(self):
        print(self.combat)

    def get_trade(self):
        print(self.trade)

    def get_regen(self):
        print(self.regen)

class baseSet(ship):
    def __init__(self, key, name, cost, faction, base_card, combat, trade, regen): ## 5 values
        super().__init__(key, name, cost, faction, combat, trade, regen)
        self.base_card = base_card ## boolean

    def is_base_set(self):
        print(base_card)


class base(ship):
    def __init__(self, key, name, cost, faction, combat, trade, regen, hp, outpost): ## 10 values
        super().__init__(key, name, cost, faction, combat, trade, regen)
        self.hp = hp ## int
        self.outpost = outpost ## boolean

    def get_hp(self):
        print(self.hp)

    def is_outpost(self):
        print(self.outpost)

class hand():
    def __init__(self, player, cards_in_hand):
        self.player = player ## strings
        self.cards_in_hand = cards_in_hand ## array

    def get_hand(self):
        print(self.cards_in_hand)

    def append(self):




s1 = baseSet('s1', "scout", 0, "n/a", True, 0, 1, 0)
s2 = baseSet('s2', "scout", 0, "n/a", True, 0, 1, 0)
s3 = baseSet('s3', "scout", 0, "n/a", True, 0, 1, 0)
s4 = baseSet('s4', "scout", 0, "n/a", True, 0, 1, 0)
s5 = baseSet('s5', "scout", 0, "n/a", True, 0, 1, 0)
s6 = baseSet('s6', "scout", 0, "n/a", True, 0, 1, 0)
s7 = baseSet('s7', "scout", 0, "n/a", True, 0, 1, 0)
s8 = baseSet('s8', "scout", 0, "n/a", True, 0, 1, 0)
v1 = baseSet('v1', "viper", 0, "n/a", True, 1, 0, 0)
v2 = baseSet('v2', "viper", 0, "n/a", True, 1, 0, 0)

b1 = ship('b1', "battle blob", 6, "blob", 8, 0, 0)
b2 = ship('b2', "blob fighter", 1, "blob", 3, 0, 0)
b3 = base('b3', "blob wheel", 3, "blob", 1, 0, 0, 5, False)
b4 = ship('b4', "battle pod", 6, "blob", 4, 0, 0)
b5 = ship('b5', "battle pod", 6, "blob", 4, 0, 0)
b6 = ship('b6', "blob destroyer", 6, "blob", 4, 0, 0)
b7 = ship('b7',"blob destroyer", 6, "blob", 4, 0, 0)
b8 = ship('b8', "blob fighter", 6, "blob", 3, 0, 0)
b9 = ship('b9', "blob fighter", 6, "blob", 3, 0, 0)
b10 = ship('b10', "blob fighter", 6, "blob", 3, 0, 0)
b11 = base('b11', "blob wheel", 3, "blob", 1, 0, 0, 5, False)
b12 = base('b12', "blob wheel", 3, "blob", 1, 0, 0, 5, False)
b13 = base('b13', "blob wheel", 3, "blob", 1, 0, 0, 5, False)
b14 = base('b14', "blob world", 8, "blob", 5, 0, 0, 7, False)
b15= ship('b15', "ram", 3, "blob", 5, 0, 0)
b16 = ship('b16', "ram", 3, "blob", 5, 0, 0)
b17 = base('b17', "the hive", 5, "blob", 3, 0, 0, 5, False)
b18 = ship('b18', "trade pod", 2, "blob", 0, 3, 0)
b19 = ship('b19', "trade pod", 2, "blob", 0, 3, 0)
b20 = ship('b20', "trade pod", 2, "blob", 0, 3, 0)


## settings for player 1's deck at round 1
deck1 = [s1, s2, s3, s4, s5, s6, s7, s8, v1, v2]
hand1 = hand('player1',[])
discard = []
discardpile = []



## player 2 assets
deck2 = [s1, s2, s3, s4, s5, s6, s7, s8, v1, v2]
hand2 = []
discard2 = []
discardpile2 = []

## shared assets
maindeck = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20]
shop = []
scrappile = []

# # deck shuffling function
import random
from random import shuffle

def shuffledeck(deck1):
    shuffle(deck1)
    return deck1

shuffle(deck1)
print(deck1)

max_hand_size = 5

## draw 5 cards from deck each round

## draw 3 cards from deck as player 1 round 1
def drawhand3(hand):
    x = 0
    for i in range(3):
        hand.append(deck[x])
        deck.remove(deck[x])
    print(hand)

def drawhand(hand):
    x = 0
    for i in range(max_hand_size):
        hand.append(deck[x])
        deck.remove(deck[x])
    print(hand)

## moving cards from hand to discard pile

def discardhand(hand):
    x = 0
    for i in range((len(hand))):
        discardpile.append(hand[x])
        hand.remove(hand[x])
    print(hand)

## function to remove a card from the opponent's hand
def discardhand_no1(hand):
    x = int(input("select opponent's card to discard: "))
    discardpile.append(hand[x-1])
    hand.remove(hand[x-1])

drawhand(hand)
discardhand_no1(hand)
print(hand)

## shuffling maindeck

## show shop each round
def showshop(maindeck):
    x = 0
    for i in range(5):
        shop.append(maindeck[x])
        maindeck.remove(maindeck[x])
    print("the shop: " + str(shop))





