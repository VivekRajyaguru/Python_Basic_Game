import random
from classes.magic import Spell
class Person:
    def __init__(self,name, hitpoint, magicpoint, attack, defence, magic, items):
        self.name = name
        self.maxhp = hitpoint
        self.hp = hitpoint
        self.maxmp = magicpoint
        self.mp = magicpoint
        self.atkl = attack - 10
        self.atkh = attack + 10
        self.df = defence
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["damage"] - 5
        mgh = self.magic[i]["damage"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]


    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":" + item)
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic")
        for item in self.magic:
            print(str(i) + ":"+ item.name, "(Cost)", item.cost)
            i += 1

    def heal(self, damage):
        self.hp += damage
        if (self.hp > self.maxhp):
            self.hp = self.maxhp

    def choose_items(self):
        i = 1
        for item in self.items:
            print(str(i) + "-" + item["item"].name + ":" + item["item"].description, "(x " + str(item.quantity) +")")
            i += 1

    def get_stats(self):
        print(str(self.name) + " HP " + str(self.hp)+"/"+str(self.maxhp)
              +"  MP "+ " " + str(self.mp)+"/"+str(self.maxmp))

    def get_enemy_stats(self):
        print(str(self.name))

    def choose_enemy(self, enemies):
        i = 1
        for item in enemies:
            print("  "+ str(i)+"  "+item.name)
            i += 1
        choice = int(raw_input(" Choose Input: ")) - 1
        return choice