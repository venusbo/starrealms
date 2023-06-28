

import random

starting_hand = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
card_pool = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 30, 30]

## introduction
print("      ")
print("*___*____*___*___*___*___*___*___*___*___*___*___*___*___*___*")
print("Welcome to Card-Scramble! AIM: collect the legendary 30 card within 13 rounds")
print("Start by drawing 5 cards from your deck and buy 1 card from the shop each turn with your hand's gold value")
print("*___*____*___*___*___*___*___*___*___*___*___*___*___*___*___*")

##seting up first round
##draw a card from the deck

round_no = 1
no_of_rounds = 13




"r" == 1

while round_no <= no_of_rounds and 30 not in starting_hand:

    hand = random.sample(starting_hand, k=5)
    hand_value = sum(hand)
    print("    ROUND: " + str(round_no))
    print(hand)
    print("your hand's gold value is = " + str(hand_value))

    ## shop
    shop = random.sample(card_pool, k=5)
    selection = input("Select a card from the pool: " + str(shop) + " ")



    ## making sure input is in shop
    exists_count = shop.count(int(selection))

    if hand_value >= int(selection) and exists_count >= 1:
        starting_hand.append(int(selection))
        card_pool.remove(int(selection))
        round_no += 1

    elif hand_value < int(selection):
        print("you don't have enough gold or invalid choice")
        selection = input("Select a card from the pool: " + str(shop) + " ")

    elif exists_count == 0:
        print("INVALID CHOICE BUSTER")
        print("SELECT A VALID CHOICE OR TYPE 'refresh' TO REFRESH THE SHOP AT THE COST OF A ROUND")
        selection = input("Select a card from the pool: " + str(shop) + " ")
        if selection == "refresh":
            round_no += 1
        elif hand_value >= int(selection) and exists_count >= 1:
            starting_hand.append(int(selection))
            card_pool.remove(int(selection))
            round_no += 1

    if selection == "refresh":
        round_no += 1

if 30 in (starting_hand):
    print("Winner Winner Chicken Dinner")
elif 30 not in (starting_hand):
    print("you lose, try again")











