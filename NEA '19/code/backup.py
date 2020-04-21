# Veer Vohra 11KWI Dubai College
# 2019 AQA GCSE Computer Science NEA
# Celebrity Dog Game

import random , time

def intro():
    ##### Main Menu #####
    choice = input("------------------------------\nWelcome to Celebrity Dogs Game\n1 - Play Game\n2 - Quit\n>>> ")
    while choice != '1' and choice != '2':
        choice = input("ERROR\nInvalid Option\nPlease Try Again\n>>>")
    if choice == '1':
        main()
    else:
        print("------------------------------ Bye ------------------------------")
        quit()

def playerwin(player_pile , cmp_pile):
    player_pile.append(player_pile[0])
    player_pile.pop(0)
    player_pile.append(cmp_pile[0])
    cmp_pile.pop(0)

def cmpwin(player_pile , cmp_pile):
    cmp_pile.append(cmp_pile[0])
    cmp_pile.pop(0)
    cmp_pile.append(player_pile[0])
    player_pile.pop(0)

def main():
    ##### Variables #####
    player_pile , cmp_pile , dog_cards , deck = [] , [] , [] , []

    ##### File Handling #####
    with open('dogs.txt') as file:
        file = file.readlines()
    file = [x.strip() for x in file]

    ##### Card Creation #####
    for dog in file:
        exercise , intelligence , friendliness , drool = random.randint(1,5) , random.randint(1,100) , random.randint(1,10) , random.randint(1,10)
        deck.append([dog, exercise , intelligence , friendliness , drool])

    ##### Number of Cards #####
    cards = input("Number of Cards : ")
    while True:
        try:
            cards = int(cards)
            if cards < 4 or cards > 30 or (cards % 2) != 0:
                raise Exception
        except Exception:
            print("Card count must be a NUMBER inbetween 4 and 30 (inclusive)\n____________________\n")
            intro()
        else:
            cards = int(cards)
            for i in range(int(cards)):
                dog_cards.append(random.choice(deck))
            break

    ##### Dealing #####
    half = int((len(dog_cards) / 2))
    for i in range(half):
        player_pile.append(dog_cards[i])
    for i in range(half):
        cmp_pile.append(dog_cards[half])
        half += 1

    ##### Game #####
    while len(player_pile) != cards and len(cmp_pile) != cards:
        print('____________________\nYour Card: ',player_pile[0][0],'\n(1)Exercise : ',player_pile[0][1],' / 5\n(2)Intelligence : ',player_pile[0][2],' / 100\n(3)Friendliness : ',player_pile[0][3],' / 10\n(4)Drool : ',player_pile[0][4],' / 10')
        category = input("Please select a characteristic\n>>> ")
        while category != '1' and category != '2' and category != '3' and category != '4':
            category = input("ERROR\nPlease enter one of the categories\n>>> ")
        print('____________________\nMy Card: ',cmp_pile[0][0],'\n(1)Exercise : ',cmp_pile[0][1],' / 5\n(2)Intelligence : ',cmp_pile[0][2],' / 100\n(3)Friendliness : ',cmp_pile[0][3],' / 10\n(4)Drool : ',cmp_pile[0][4],' / 10')
        if category == '1':
            if player_pile[0][1] >= cmp_pile[0][1]:
                print("____________________\nCATEGORY : Exercise\nYOU WIN\n____________________")
                playerwin(player_pile , cmp_pile)
            elif player_pile[0][1] < cmp_pile[0][1]:
                print("____________________\nCATEGORY : Exercise\nYOU LOSE\n____________________")
                cmpwin(player_pile , cmp_pile)

        elif category == '2':
            if player_pile[0][2] >= cmp_pile[0][2]:
                print("____________________\nCATEGORY : Intelligence\nYOU WIN\n____________________")
                playerwin(player_pile , cmp_pile)
            elif player_pile[0][2] < cmp_pile[0][2]:
                print("____________________\nCATEGORY : Intelligence\nYOU LOSE\n____________________")
                cmpwin(player_pile , cmp_pile)

        elif category == '3':
            if player_pile[0][3] >= cmp_pile[0][3]:
                print("____________________\nCATEGORY : Friendliness\nYOU WIN\n____________________")
                playerwin(player_pile , cmp_pile)
            elif player_pile[0][3] < cmp_pile[0][3]:
                print("____________________\nCATEGORY : Friendliness\nYOU LOSE\n____________________")
                cmpwin(player_pile , cmp_pile)

        elif category == '4':
            if player_pile[0][4] <= cmp_pile[0][4]:
                print("____________________\nCATEGORY : Drool\nYOU WIN\n____________________")
                playerwin(player_pile , cmp_pile)
            elif player_pile[0][4] > cmp_pile[0][4]:
                print("____________________\nCATEGORY : Drool\nYOU LOSE\n____________________")
                cmpwin(player_pile , cmp_pile)

        time.sleep(2)

    if len(player_pile) == cards:
        print("YOU WIN\nWELL DONE")
    else:
        print("I WIN\nUNLUCKY")
    intro()

intro()
