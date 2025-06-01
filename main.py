import os
import time
import random


done_intro = False

p1_cards = []
p2_cards = []
p1_coins = 0
p2_coins = 0
give_start = 4

#  first argument is the description, second is health, third is damage, fourth is defense, and fifth is rarity


computer_card = ["Keyboard", "Mouse", "Monitor", "FireFox", "CPU", "GPU", "Google", "Gaming PC", "Supercomputer", "Quantum Computer"]

computer_card_stats = [
                        ["Click clack", 25, 10, 5, "Normal"], 
                        ["Click.", 25, 7, 5, "Normal"], 
                        ["Shows stuff.", 40, 3, 2, "Normal"], 
                        ["Browse.", 17.5, 10, 7, "Uncommon"], 
                        ["Finishes tasks quickly but vulnerable to heat.", 12.5, 15, 5, "Uncommon"], 
                        ["Great for taking down groups.", 15, 5, 10, "Rare"], 
                        ["Better than FireFox.", 25, 10, 5, "Rare"], 
                        ["Made for gaming", 35, 15, 10, "Epic"], 
                        ["Superfast!", 30, 10, 20, "Epic"],
                        ["Quantum physics!", 30, 17, 15, "Legendary"],
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
            return (c2_hp - c1_atk + c2_defed), c2_hp, c2_defed

    elif wcf == 2:
        c1_defed = random.randint(1, c1_def)
        if (c2_atk - c1_def) <= 0:
            return c1_hp, c1_hp, c1_defed
        else:
            return (c1_hp - c2_atk + c1_defed), c1_hp, c1_defed
    

def roll_start():
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

while True:
    if done_intro == False:
        intro_1 = input("Welcome to Card Battle! Find a friend to play with you. Press on 'c' to continue. ")
        if intro_1 == "c":
            sleep(0)
            intro_2 = input("Now decide who will be player 1 and who will be player 2. Press on 'c' to continue. ")
            if intro_2 == "c":
                sleep(0)
                intro_3 = input("Player 1 and Player 2, you will both receive 4 random cards. Press 'c' to continue. ")
                roll_start()
                if intro_3 == "c":
                    sleep(0)
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
        menu_option = input("1. Play \n2. View your deck\n3. Get more cards \nChoice: ")
        if menu_option == "1":
            print(f"Player 1 has: {', '.join(p1_cards)}")
            print(f"Player 2 has: {', '.join(p2_cards)}") 
            m1_1 = input("Press c to continue: ")
            if m1_1 == "c":
                going = 1
                print(f"Player 1 has: {', '.join(p1_cards)}")
                print(f"Player 2 has: {', '.join(p2_cards)}")
                temp1 = [{p1_cards[0]: computer_card_stats[computer_card.index(p1_cards[0])][1]}, 
                            {p1_cards[1]: computer_card_stats[computer_card.index(p1_cards[1])][1]},
                            {p1_cards[2]: computer_card_stats[computer_card.index(p1_cards[2])][1]},
                            {p1_cards[3]: computer_card_stats[computer_card.index(p1_cards[3])][1]}]
                temp2 = [{p2_cards[0]: computer_card_stats[computer_card.index(p2_cards[0])][1]},
                            {p2_cards[1]: computer_card_stats[computer_card.index(p2_cards[1])][1]},
                            {p2_cards[2]: computer_card_stats[computer_card.index(p2_cards[2])][1]},
                            {p2_cards[3]: computer_card_stats[computer_card.index(p2_cards[3])][1]}]
                while True:
                    c1_w = False
                    c2_w = False
                    m1_p1 = input("Player 1 card: ")
                    if m1_p1 in p1_cards:
                        m1_p2 = input("Player 2 card: ")
                        if m1_p2 in p2_cards:
                            print(f"Player 1 chose {m1_p1}! Player 2 chose {m1_p2}!")
                            if m1_p1 in computer_card:
                                c1_stats = computer_card_stats[computer_card.index(m1_p1)]
                                c1_hp = next((d[m1_p1] for d in temp1 if m1_p1 in d), None)
                                c1_atk = c1_stats[2]
                                c1_def = c1_stats[3]
                            if m1_p2 in computer_card:
                                c2_stats = computer_card_stats[computer_card.index(m1_p2)]
                                c2_hp = next((d[m1_p2] for d in temp2 if m1_p2 in d), None)
                                c2_atk = c2_stats[2]
                                c2_def = c2_stats[3]
                            if going == 1:
                                c2_hpn, c2_hp, c2_defed = battle(c1_hp, c1_atk, c1_def, c2_hp, c2_atk, c2_def, 1)
                                print(f"Player 1's {m1_p1} goes first! It does {(c2_hp - c2_hpn) + c2_defed} damage {m1_p2} blocks {c2_defed} damage! {m1_p2} now has {c2_hpn} HP!")
                                next(d for d in temp2 if m1_p2 in d)[m1_p2] = c2_hpn
                                if c2_hp <= 0:
                                    temp2.remove(next(d for d in temp2 if m1_p2 in d))
                                    print(temp2)
                                    if len(temp2) == 0:
                                        c1_w = True
                                    break
                                else:
                                    going = 2
                            elif going == 2:
                                c1_hpn, c1_hp, c1_defed = battle(c1_hp, c1_atk, c1_def, c2_hp, c2_atk, c2_def, 2)
                                print(f"Player 2's {m1_p2} goes first! It does {(c1_hp - c1_hpn) + c1_defed} damage {m1_p1} blocks {c1_defed} damage! {m1_p1} now has {c1_hpn} HP!") 
                                next(d for d in temp1 if m1_p1 in d)[m1_p1] = c1_hpn
                                if c1_hp <= 0:
                                    temp1.remove(next(d for d in temp1 if m1_p1 in d))
                                    print(temp1)
                                    if len(temp1) == 0:
                                        c2_w = True
                                    break
                                else:
                                    going = 1
                            time.sleep(1)
                        else:
                            print("Invalid card. Try again. ()") 
                    else:
                        print("Invalid card. Try again.")
            if c1_w == True:
                print("Player 1 wins!")
                p1_coins += 50
                p2_coins += 15
                print("P1: +50 coins \n P2: +15 coins")
            elif c2_w == True:
                print("Player 2 wins!")
                p1_coins += 15
                p2_coins += 50
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
            m3_going = True
            while m3_going == True:
                while True:
                    m3 = input("Player 1 or Player 2? Or press 'c' to exit. \nChoice: ")
                    if m3 == "1":
                        if p1_coins >= 50:
                            m3_1 = input(f"You have {p1_coins} coins. Which pack are you going to choose from? Packs: {', '.join(pack_names)} \nPack: ")
                            if m3_1 == "Computer Pack":
                                m3_1_1 = random.choice(all_packs[0])
                                p1_cards.append(m3_1_1)
                                print(f"Player 1 received {m3_1_1}!")
                                sleep(0.5) 
                                break
                        else:
                            print("You don't have enough coins.")
                            sleep(0.5) 
                            break       
                    elif m3 == "2":
                        if p2_coins >= 50:
                            m3_2 = input(f"You have {p2_coins} coins. Which pack are you going to choose from? Packs: {', '.join(pack_names)} \nPack: ")
                            if m3_2 == "Computer Pack":
                                m3_2_1 = random.choice(all_packs[0])
                                p2_cards.append(m3_2_1)
                                print(f"Player 2 received {m3_2_1}!")
                                sleep(0.5)
                        else:
                            print("You don't have enough coins.")
                            sleep(0.5)
                            break
                    elif m3 == "c":
                        print("Exiting...")
                        m3_going = False
                        sleep(0.5)
                        break
                    else:
                        print("Invalid player.")
                        sleep(0.5)
        else:
            print("Invalid option.")
            sleep(0.5)
            pass