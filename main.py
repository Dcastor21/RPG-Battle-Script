from classes.game import Person, bcolors
from classes.magic import Spell

fire= Spell("Fire", 10, 100,"Black")
thunder = Spell("Thunder", 10, 100,"Black")
blizzard = Spell("Blizarrd", 10, 100,"Black")
poison = Spell("Blizarrd", 10, 100,"Black")
earthquake = Spell("Blizarrd", 10, 100,"Black")

cure = Spell("Cure", 15, 150, "White")
cura = Spell("Cura", 18, 200, "white")



player = Person(460, 40, 60, 36, [fire, blizzard, poison, earthquake])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC + " this is normal")

while running:
    print("===============================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("your attacked  for", dmg, "points of damage.")
    

    elif index == 1:
        player.choose_magic_spell()
        magic_choice = int(input("Choose magic:")) - 1

        spell = Player.magic[Magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for",enemy_dmg, "Player HP",player.get_hp())

    print("----------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/"+ str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("your HP:", bcolors.OKGREEN + str(player.get_hp()) +"/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors. ENDC + "\n")

    
    if enemy.get_hp()== 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
        
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lose!" + bcolors.ENDC)
        
