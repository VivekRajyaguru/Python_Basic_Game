import os, sys
import random
from classes.game import Person
from classes.magic import Spell
from classes.inventory import Item

# Black Magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 12, 120, "Black")

# White Magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

# create Some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully Restored HP/MP one member", 9999)
helixer = Item("Mega Elixer", "elixer", "Fully Restored HP/MP", 9999)

granade = Item("Grenade", "attack", "Attack 500 HP", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cura, cure]
player_items = [{"item": potion, "quantity": 5}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": helixer, "quantity":5}, {"item": granade, "quantity":5}]

# Instantiate People
player1 = Person("Vivek", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Test", 460, 70, 50, 50, player_spells, player_items)
player3 = Person("Test 2", 500, 80, 40, 30, player_spells, player_items)

enemy1 = Person("Enemy1", 1200, 65, 45, 25, [], [])
enemy2 = Person("Enemy2", 100, 40, 50, 20, [], [])
enemy3 = Person("Enemy3", 200, 50, 50, 30, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

while running:
    print("===============================")

    print("\n\n")
    for player in players:
        player.get_stats()

    for enemy in enemies:
        enemy.get_enemy_stats();


    print("\n")
    for player in players:

        player.choose_action()
        choice = raw_input("Please Select Action:")
        index = int(choice) - 1

        if index == 0:
            damage = player.generate_damage()
            enemy.take_damage(damage)
            print(player.name + " has done "+ str(damage) + "to Enemy")

        elif index == 1:
            player.choose_magic()
            magic_choice = raw_input("Choose Magic");
            magic_index = int(magic_choice) - 1

            spell = player.magic[magic_index]
            magic_damage = spell.generate_damage()

            current_mp = player.get_mp()
            if spell.cost > current_mp:
                print ("No Enough MP")
                continue

            player.reduce_mp(spell.cost)
            if spell.type == "White":
                player.heal(magic_damage)
                print("You Heal for ", magic_damage,"Points")
            elif spell.type == "Black":
                enemy.take_damage(magic_damage)
                print("You Attack for ", magic_damage," Points. Enemy HP:", enemy.get_hp())

        elif index == 2:
            player.choose_items()
            item_index = int(raw_input("Select Item")) - 1
            item = player.items[item_index]["item"]

            if player.items[item_index]["quantity"] == 0:
                print("None Left")
                continue

            player.items[item_index]["quantity"] -= 1

            if item.type == 'potion':
                player.heal(item.prop)
            elif item.type == 'attack':
                enemy.take_damage(item.prop)
            elif item.type == 'elixer':
                player.hp = player.maxhp
                player.mp = player.mp

        enemy_target = int(random.randrange(0, 2))
        enemy_choice = 1
        enemy_damage = enemy.generate_damage()
        players[enemy_target].take_damage(enemy_damage)

        if player.get_hp() == 0 or enemy.get_hp() == 0:
            if player.get_hp() == 0:
                print("Player is Dead. Enemy Wins.")
            else:
                print("Enemy is Dead. Player Wins")
            running = False
