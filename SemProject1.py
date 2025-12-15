#Name:alaya
#Class: 6th Hour
#Assignment: Semester Project 1

import random


#Due to weird time travelling circumstances beyond explanation, you find yourself in 2018 or so
#working for Larian Studios. Currently, they are working on the early prototypes of the hype
#upcoming game "Baldur's Gate 3". BG3 is a game that uses the Dungeons & Dragons 5th edition rules
#as its framework for gameplay. You have been given a basic dictionary of some of the main hero
#characters and some of the enemies they may face, and are tasked with making an early prototype
#of one of the party members fighting against an enemy until one of them hits zero HP (dies).

partyDict = {
    "LaeZel" : {
        "HP" : 48,
        "Init" : 1,
        "AC" : 17,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },}


enemyDict = {

    "Mindflayer": {
        "HP" : 71,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + 4
    ,},}

#Combat consists of these steps:

#1. Rolling for 'initiative' to see who goes first. This is determined by rolling a
#20-sided die (d20) and adding their initiative modifier (If the roll is the same,
#assume the hero goes first).
player = partyDict["LaeZel"]
enemy = enemyDict["Mindflayer"]

player_init = random.randint(1,20)+player["Init"]
enemy_init = random.randint(1,20)+enemy["Init"]

print("LaeZel's Inititative:" , player_init)
print("Mindflayer's Initiative:" , enemy_init)

if enemy_init >= player_init:
    print("Mindflayer Goes First!")
    attacker = enemy
    defender = player
else:
    print("LaeZel Goes First")
    attacker = player
    defender = enemy
#2. Rolling to attack. This is determined by rolling a 20-sided die (d20) and adding their
#attack modifier. The attack hits if it matches or is higher than the target's Armor Class (AC).
#If the d20 rolled to attack is an unmodified ("natural") 20, the attack automatically hits and
#the character deals double damage. If the d20 rolled to attack is an unmodified ("natural") 1,
#the attack automatically misses

while player["HP"] >0 and enemy["HP"] > 0:

    if attacker == enemy:
        roll = random.randint(1,20)
        print("Mindflayer's Roll :" , roll)

        if roll == 1:
            print("You suck. Automatic Miss.")
            attacker = player
        else: hit_value = roll+enemy["AtkMod"]

        if roll == 20:
            print("wow youre amzing good job automatic hit")
            dmg = enemy["Damage"]*2
            player["HP"] -= dmg
            print("Mindflayer's Damage:" , dmg)
            attacker = player
        elif hit_value >= player["AC"]:
            dmg = enemy["Damage"]
            player["HP"] -= dmg
            print("Mindflayer's Damage:" , dmg)
            attacker = player
        else:
            print("Mindflayer misses")
            attacker = player




#3. If the attack hits, roll damage and subtract it from the target's hit points.

#4. The second in initiative rolls to attack (and rolls damage) afterwards.

#5. Repeat steps 2-5 until one of the characters is dead

