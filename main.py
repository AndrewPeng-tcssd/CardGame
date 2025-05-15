import os
import time
import random

done_intro = False

p1_cards = {}
p2_cards = {}

# key is the name of the card. value is an array and first argument is the description, second is health, third is damage, fourth is defense, and fifth is how many cards at once and sixth is rarity
computer_cards = {
        "Keyboard": ["Whacks the opponent.", 50, 25, 5, 1, "Normal"], 
        "Mouse": ["Clicking power!", 75, 15, 5, 1, "Normal"], 
        "Monitor": ["Brainwashes your opponent with memes.", 100, 10, 10, 1, "Normal"], 
        "FireFox": ["Overwelmes your opponent with tons of websites.", 15, 15, 1.25, 1, "Normal"],
        "CPU": ["Finishes tasks quickly but vulnerable.", 25, 35, 2.5, 1, "Uncommon"],
        "GPU": ["Great for taking down groups.", 30, 10, 2.5, 5, "Uncommon"],
        "Google": ["Overwelmes your opponent. Better than FireFox.", 25, 20, 2, 1, "Uncommon"],
        "Razer Gaming Keyboard 1.0": ["Whacks the opponent and packed with LED lights.", 65, 35, 7.5, 1, "Epic"],
        "Predator Mouse M1": ["Neon clicking power!", 80, 25, 7.5, 1, "Epic"]
}


stuff_cards = {
    "Pencil": ["Writes stuff.", 15, 15, 2.5, 1, "Normal"]
}


def sleep(sleep_time):
    time.sleep(sleep_time)
    os.system("clear")

while True:
    if done_intro == False:
        intro_1 = input("Welcome to Card Battle! Find a friend to play with you. Press on any key to continue. ")
        if intro_1:
            intro_2 = input("Now decide who will be player 1 and who will be player 2. Press on any key to continue.")
            if intro_2:
                intro_3 = input("Player 1 and Player 2, you will both receive 4 random cards. Press on any key to continue.")
                for i in range(4):
                    if i == 1 or i == 3:
                        random_num = random.randint(1, 100)
                        if 1 <= random_num <= 60:
                            random_num_common = random.randint(1, 4)
                            whichcard = random_num_common
                        elif 61 <= random_num <= 90:
                            random_num_uncommon = random.randint(1, 3)
                            whichcard = random_num_uncommon
                        elif 91 <= random_num <= 100:
                            random_num_epic = random.randint(1, 2)
                            whichcard = random_num_epic
                        whichkey = list(computer_cards.keys())[whichcard - 1]
                        p1_cards[whichkey] = computer_cards[whichkey]

                    elif i == 2 or i == 4:
                        random_num = random.randint(1, 100)
                        if 1 <= random_num <= 60:
                            random_num_common = random.randint(1, 4)
                            whichcard = random_num_common
                        elif 61 <= random_num <= 90:
                            random_num_uncommon = random.randint(1, 3)
                            whichcard = random_num_uncommon
                        elif 91 <= random_num <= 100:
                            random_num_epic = random.randint(1, 2)
                            whichcard = random_num_epic
                        whichcard = random.randint(1, len(stuff_cards))
                        whichkey = list(stuff_cards.keys())[whichcard - 1]
                        p1_cards[whichkey] = stuff_cards[whichkey]



                for i in range(4):
                    rand_pack_p2 = random.randint(1, 2)
                    if rand_pack_p2 == 1:
                        random_num = random.randint(1, 100)
                        if 1 <= random_num <= 60:
                            random_num_common = random.randint(1, 4)
                            whichcard = random_num_common
                        elif 61 <= random_num <= 90:
                            random_num_uncommon = random.randint(1, 3)
                            whichcard = random_num_uncommon
                        elif 91 <= random_num <= 100:
                            random_num_epic = random.randint(1, 2)
                            whichcard = random_num_epic
                        whichcard = random.randint(1, len(computer_cards))
                        whichkey = list(computer_cards.keys())[whichcard - 1]
                        p2_cards[whichkey] = computer_cards[whichkey]

                    elif rand_pack_p2 == 2:
                        random_num = random.randint(1, 100)
                        if 1 <= random_num <= 60:
                            random_num_common = random.randint(1, 4)
                            whichcard = random_num_common
                        elif 61 <= random_num <= 90:
                            random_num_uncommon = random.randint(1, 3)
                            whichcard = random_num_uncommon
                        elif 91 <= random_num <= 100:
                            random_num_epic = random.randint(1, 2)
                            whichcard = random_num_epic
                        whichcard = random.randint(1, len(stuff_cards))
                        whichkey = list(stuff_cards.keys())[whichcard - 1]
                        p1_cards[whichkey] = stuff_cards[whichkey]

                if intro_3:
                    intro_4 = input(f"Player 1 received: ")
        else:
            print("Invalid")
        done_intro = True

            