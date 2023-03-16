import random

# Race options
races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']

# Class options
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

# Background options
backgrounds = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit', 'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']

# Ability scores
ability_scores = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

# Define function for rolling ability scores
def roll_ability_score():
    dice_rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(dice_rolls, reverse=True)[:3])

# Randomly select race, class, background and generates ability scores
race = random.choice(races)
character_class = random.choice(classes)
character_background = random.choice(backgrounds)
ability_scores = [roll_ability_score() for _ in range(6)]

# Print character information
print('Race:', race)
print('Class:', character_class)
print('Background:', character_background)
print('Ability Scores:')
print(f"STR: {ability_scores[0]}")
print(f"DEX: {ability_scores[1]}")
print(f"CON: {ability_scores[2]}")
print(f"INT: {ability_scores[3]}")
print(f"WIS: {ability_scores[4]}")
print(f"CHA: {ability_scores[5]}")
