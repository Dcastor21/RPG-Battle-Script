from classes.game import Person,bbcolors

magic = [{"name": "Fire", "Cost":10, "dmg":25},
         {"name": "Thunder", "Cost":10, "dmg":60},
         {"name": "Blizzard", "Cost":15, "dmg":30}]


player = Person(460, 65, 60, 36, magic)

print(player.generate_damage())