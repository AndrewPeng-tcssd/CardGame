import os
import time
import random
from getpass import getpass


done_intro = False

p1_cards = []
p2_cards = []
p1_coins = 50
p2_coins = 50
give_start = 4

# key is the name of the card value is an array and first argument is the description, second is health, third is damage, fourth is defense, and fifth is rarity


computer_card = ["Keyboard", "Mouse", "Monitor", "FireFox", "CPU", "GPU", "Google", "Gaming PC", "Supercomputer", "Quantum Computer"]

computer_card_stats = [
                        ["Click clack", 50, 10, 5, "Normal"], 
                        ["Click.", 50, 7, 5, "Normal"], 
                        ["Shows stuff.", 80, 3, 2, "Normal"], 
                        ["Browse.", 35, 10, 7, "Uncommon"], 
                        ["Finishes tasks quickly but vulnerable to heat.", 25, 15, 5, "Uncommon"], 
                        ["Great for taking down groups.", 30, 5, 10, "Rare"], 
                        ["Better than FireFox.", 50, 10, 5, "Rare"], 
                        ["Made for gaming", 70, 15, 10, "Epic"], 
                        ["Superfast!", 60, 10, 20, "Epic"],
                        ["Quantum physics!", 60, 17, 15, "Legendary"],
                    ]





pack_names = ["Computer Pack"]

all_packs = [computer_card]


def sleep(sleep_time):
    time.sleep(sleep_time)
    os.system("clear")

def battle(c1_hp, c1_atk, c1_def, c2_hp, c2_atk, c2_def, wcf):
    #if c1 in computer_card:
        #c1_stats = computer_card_stats[computer_card.index(c1)]
    #if c2 in computer_card:
        #c2_stats = computer_card_stats[computer_card.index(c2)]
    if wcf == 1:
        c2_defed = random.randint(1, c2_def)
        if (c1_atk - c2_defed) <= 0:
            return c2_hp, c2_hp, c1_defed
        else:
            return (c2_hp - (c1_atk - c2_defed)), c2_hp, c2_defed

    elif wcf == 2:
        c1_defed = random.randint(1, c1_def)
        if (c2_atk - c1_def) <= 0:
            return c1_hp, c1_hp, c1_defed
        else:
            return (c1_hp - (c2_atk - c1_defed)), c1_hp, c1_defed
    

    

while True:
    if done_intro == False:
        intro_1 = input("Welcome to Card Battle! Find a friend to play with you. Press on 'c' to continue. ")
        if intro_1 == "c":
            sleep(0.5)
            intro_2 = input("Now decide who will be player 1 and who will be player 2. Press on 'c' to continue. ")
            if intro_2 == "c":
                sleep(0.5)
                intro_3 = input("Player 1 and Player 2, you will both receive 4 random cards. Press 'c' to continue. ")
                for i in range(give_start): 
                    which_pack = random.choice(all_packs)
                    random_num = random.randint(1, 100)
                    if 1 <= random_num <= 60:
                        random_num_common = random.randint(0, 3)
                        whichcard = random_num_common
                    elif 61 <= random_num <= 90:
                        random_num_uncommon = random.randint(4, 7)
                        whichcard = random_num_uncommon
                    elif 91 <= random_num <= 99:
                        random_num_epic = random.randint(8, 9)
                        whichcard = random_num_epic
                    elif random_num == 100:
                        whichcard = 9
                    p1_cards.append(which_pack[whichcard])


                for i in range(give_start):
                    which_pack = random.choice(all_packs)
                    random_num = random.randint(1, 100)
                    if 1 <= random_num <= 60:
                        random_num_common = random.randint(0, 3)
                        whichcard = random_num_common
                    elif 61 <= random_num <= 90:
                        random_num_uncommon = random.randint(4, 7)
                        whichcard = random_num_uncommon
                    elif 91 <= random_num <= 99:
                        random_num_epic = random.randint(8, 9)
                        whichcard = random_num_epic
                    elif random_num == 100:
                        whichcard = 9
                    p2_cards.append(which_pack[whichcard])

                if intro_3 == "c":
                    sleep(1)
                    print(f"Player 1 received: {', '.join(p1_cards)}")
                    print(f"Player 2 received: {', '.join(p2_cards)}")
                    intro_3_1 = input("Press c to continue: ")
                    if intro_3_1 == "c":
                        sleep(0)
                        done_intro = True
                    else:
                        pass

    else:
        sleep(0)
        menu_option = input("""
                    1. Play
                    2. View your deck
                    3. Get more cards
                    (type in the number) """)
        if menu_option == "1":
            print(f"Player 1 has: {', '.join(p1_cards)}")
            print(f"Player 2 has: {', '.join(p2_cards)}") 
            m1_1 = input("Press c to continue: ")
            if m1_1 == "c":
                m1_1_r1 = random.randint(1,2)
                print("Rolling.")
                sleep(0.2)
                print("Rolling..")
                sleep(0.2)
                print("Rolling...")
                if m1_1_r1 == 1:
                    print("Player 1 goes first!")
                    while True:
                        print(f"Player 1 has: {', '.join(p1_cards)}")
                        print(f"Player 2 has: {', '.join(p2_cards)}") 
                        m1_1_r1_p1_c1 = getpass("Player 1 card: ")
                        if m1_1_r1_p1_c1 in p1_cards:
                            m1_1_r1_p2_c1 = getpass("Player 2 card: ")
                            if m1_1_r1_p2_c1 in p2_cards:
                                print(f"Player 1 chose {m1_1_r1_p1_c1}! Player 2 chose {m1_1_r1_p2_c1}!")
                                if m1_1_r1_p1_c1 in computer_card:
                                    c1_stats = computer_card_stats[computer_card.index(m1_1_r1_p1_c1)]
                                    c1_hp = c1_stats[1]
                                    c1_atk = c1_stats[2]
                                    c1_def = c1_stats[3]
                                if m1_1_r1_p2_c1 in computer_card:
                                    c2_stats = computer_card_stats[computer_card.index(m1_1_r1_p2_c1)]
                                    c2_hp = c2_stats[1]
                                    c2_atk = c2_stats[2]
                                    c2_def = c2_stats[3]
                                m1_1_r2 = random.randint(1,2)
                                if m1_1_r2 == 1:
                                    c2_hpn, c2_hp, c2_defed = battle(c1_hp, c1_atk, c1_def, c2_hp, c2_atk, c2_def, 1)
                                    print(f"Player 1's {m1_1_r1_p1_c1} goes first! It does {(c2_hp - c2_hpn) + c2_defed} damage {m1_1_r1_p2_c1} blocks {c2_defed} damage! {m1_1_r1_p2_c1} now has {c2_hpn} HP!")
                                    if c2_hpn <= 0:
                                        break
                                    else:
                                        pass
                                elif m1_1_r2 == 2:
                                    c1_hpn, c1_hp, c1_defed = battle(c1_hp, c1_atk, c1_def, c2_hp, c2_atk, c2_def, 2)
                                    print(f"Player 2's {m1_1_r1_p2_c1} goes first! It does {(c1_hp - c1_hpn) + c1_defed} damage {m1_1_r1_p1_c1} blocks {c1_defed} damage! {m1_1_r1_p1_c1} now has {c1_hpn} HP!")
                                    if c1_hpn <= 0:
                                        break
                                    else:
                                        pass
                                time.sleep(1)
                            else:
                                print("Invalid card. Try again. ()") 
                        else:
                            print("Invalid card. Try again.")
                elif m1_1_r1 == 2:
                    print("Player 2 goes first!")
                    while True:
                        p1_w = False
                        p2_w = False
                        print(f"Player 1 has: {', '.join(p1_cards)}")
                        print(f"Player 2 has: {', '.join(p2_cards)}") 
                        m1_1_r2_p2_c1 = getpass("Player 2 card: ")
                        if m1_1_r2_p2_c1 in p2_cards:
                            m1_1_r2_p1_c1 = getpass("Player 1 card: ")
                            if m1_1_r2_p1_c1 in p1_cards:
                                print(f"Player 1 chose {m1_1_r2_p1_c1}! Player 2 chose {m1_1_r2_p2_c1}!")
                                if m1_1_r2_p1_c1 in computer_card:
                                    c1_stats = computer_card_stats[computer_card.index(m1_1_r2_p1_c1)]
                                    c1_hp = c1_stats[1]
                                    c1_atk = c1_stats[2]
                                    c1_def = c1_stats[3]
                                if m1_1_r2_p2_c1 in computer_card:
                                    c2_stats = computer_card_stats[computer_card.index(m1_1_r2_p2_c1)]
                                    c2_hp = c2_stats[1]
                                    c2_atk = c2_stats[2]
                                    c2_def = c2_stats[3]
                                m1_1_r2 = random.randint(1,2)
                                if m1_1_r2 == 1:
                                    c2_hpn, c2_hp, c2_defed = battle(c1_hp, c1_atk, c1_def, c2_hp, c2_atk, c2_def, 1)
                                    print(f"Player 1's {m1_1_r2_p1_c1} goes first! It does {(c2_hp - c2_hpn) + c2_defed} damage {m1_1_r2_p2_c1} blocks {c2_defed} damage! {m1_1_r2_p2_c1} now has {c2_hpn} HP!")
                                    if c2_hpn <= 0:
                                        c1_w = True
                                        break
                                elif m1_1_r2 == 2:
                                    c1_hpn, c1_hp, c1_defed = battle(c1_hp, c1_atk, c1_def, c2_hp, c2_atk, c2_def, 2)
                                    print(f"Player 2's {m1_1_r2_p2_c1} goes first! It does {(c1_hp - c1_hpn) + c1_defed} damage {m1_1_r2_p1_c1} blocks {c1_defed} damage! {m1_1_r2_p1_c1} now has {c1_hpn} HP!")
                                    if c1_hpn <= 0:
                                        c2_w = True
                                        break
                                time.sleep(1)
                            else:
                                print("Invalid card. Try again.") 
                        else:
                            print("Invalid card. Try again.")
                    if c1_w == True:
                        print("Player 1 wins!")
                        c1_w += 50
                        c2_w += 15
                        print("P1: +50 coins \n P2: +15 coins")
                    elif c2_w == True:
                        print("Player 2 wins!")
                        c1_w += 15
                        c2_w += 50
                        print("P1: +15 coins \n P2: +50 coins")



            else:
                pass
        elif menu_option == "2":
            m2 = input("Which player? (1 or 2) ")
            if m2 == "1":
                sleep(0)
                m2_1 = input(f"Player 1 has: {', '.join(p1_cards)} press c to exit or type the name of the card to see the stats. ")
                if m2_1 == "c":
                    pass
                else:
                    if m2_1 in computer_card:
                        sleep(0)
                        print("Getting stats...")
                        sleep(0.75)
                        which_index = computer_card.index(m2_1)
                        card = computer_card_stats[which_index]
                        m2_1_1 = input(f"""
                                        Info: {card[0]}
                                        HP: {card[1]}
                                        Attack: {card[2]}
                                        Defense: {card[3]}
                                        Rarity: {card[4]}
                                        type "c" to exit 
""")        
                    else:
                        print("Invalid card.")
                        sleep(1)

            elif m2 == "2":
                sleep(0)
                m2_2 = input(f"Player 2 has: {', '.join(p2_cards)} press c to exit or type the name of the card to see the stats. ")
                if m2_2 == "c":
                    pass
                else:
                    if m2_2 in computer_card:
                        sleep(0)
                        print("Getting stats...")
                        sleep(0.75)
                        which_index = computer_card.index(m2_1)
                        card = computer_card_stats[which_index]
                        m2_2_2 = input(f"""
                                        Info: {card[0]}
                                        HP: {card[1]}
                                        Attack: {card[2]}
                                        Defense: {card[3]}
                                        Rarity: {card[4]}
                                        type "c" to exit 
""")        
                    else:
                        print("Invalid card.")
                        sleep(1)
                    
        elif menu_option == "3":
            sleep(0)
            m3 = input("Player 1 or Player 2? ")
            if m3 == "1":
                m3_1 = input(f"Which pack are you going to choose from? Packs: {', '.join(pack_names)} ")
            elif m3 == "2":
                m3_1 = input(f"Which pack are you going to choose from? Packs: {', '.join(pack_names)} ")
