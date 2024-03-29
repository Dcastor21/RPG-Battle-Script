from classes.game import Person, bcolors
from classes.inventory import Item
from classes.magic import Spell
import time


print("\n\n")
# Create Black Magic
fire = Spell("Fire", 10, 1000, "black")
thunder = Spell("Thunder", 10, 1100, "black")
blizzard = Spell("Blizzard", 10, 1400, "black")
meteor = Spell("Meteor", 20, 1200, "black")
quake = Spell("Quake", 14, 1240, "black")

# Create White Magic
cure = Spell('Cure', 12, 620, "white")
cura = Spell('Cura', 12, 1220, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixr = Item("Elixr", "elixr", "Full restores party's HP/MP", 999)
hielixr = Item("MegaElixr", "elixr", "Full restores party's HP/MP", 999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 15}, {
                    "item": elixr, "quantity": 5},
                {"item": hielixr, "quantity": 5}, {"item": grenade, "quantity": 10}]


# instantiate People
player1 = Person("Valos: ", 3260, 140, 300, 34, player_spells, player_items)
player2 = Person("Nick: ", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Jason: ", 3089, 174, 288, 34, player_spells, player_items)
enemy = Person("Magnus", 11200, 701, 525, 25, [], [])

players = [player1, player2, player3]

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" +
      bcolors.ENDC + " this is normal")

while running:
    print("===============================")
    for player in players:
        print("\n\n")
        print("Name                  HP                                  MP")
        player.get_stats()

    print("\n")

    for player in players:

        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice, base=0) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("your attacked  for", dmg, "points of damage")

        elif index == 1:
            player.choose_magic_spell()
            magic_choice = int(input("Choose magic:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                time.sleep(5)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name +
                      " heals for", str(magic_dmg), "HP" + bcolors.ENDC)

            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "deals",
                      str(magic_dmg), "points of damage" + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("choose Item: ")) - 1

            if item_choice == -1:
                continue

            if player_items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None Left..." + bcolors.ENDC)
                continue

            item = player.item[item_choice]["item"]
            player_items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name +
                      "heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixr":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name +
                      "fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + "deals",
                      str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("----------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) +
          "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("your HP:", bcolors.OKGREEN + str(player.get_hp()) +
          "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("your MP:", bcolors.OKBLUE + str(player.get_mp()) +
          "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lose!" + bcolors.ENDC)
        running = False
