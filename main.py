from classes.game import Person, bcolors

magic = [{"name": "Fire", "Cost":10, "dmg":25},
         {"name": "Thunder", "Cost":10, "dmg":60},
         {"name": "Blizzard", "Cost":15, "dmg":30}]


player = Person(460, 65, 60, 36, magic)
enemy= Person(1200,65,45,25, magic)

running = True
i= 0
print(bcolors.FAIL+ bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC + "this is normal")

while running:
    print("===============================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) -1

    if  index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print ("your attacked  for", dmg, "points of damage. Enemy HP:", enemy.get_hp())

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for",enemy_dmg, "Player HP",player.get_hp())
    
    if enemy.gethp()== 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
        
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lose!" + bcolors.ENDC)
        
