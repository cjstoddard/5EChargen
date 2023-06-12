import random

# Define lists of possible character traits
races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
classes = {
    'Barbarian': {'required_score': 'STR', 'minimum_score': 15},
    'Bard': {'required_score': 'CHA', 'minimum_score': 15},
    'Cleric': {'required_score': 'WIS', 'minimum_score': 15},
    'Druid': {'required_score': 'WIS', 'minimum_score': 15},
    'Fighter': {'required_score': 'STR', 'minimum_score': 15},
    'Monk': {'required_score': 'DEX', 'minimum_score': 15},
    'Paladin': {'required_score': 'STR', 'minimum_score': 15},
    'Ranger': {'required_score': 'DEX', 'minimum_score': 15},
    'Rogue': {'required_score': 'DEX', 'minimum_score': 15},
    'Sorcerer': {'required_score': 'CHA', 'minimum_score': 15},
    'Warlock': {'required_score': 'CHA', 'minimum_score': 15},
    'Wizard': {'required_score': 'INT', 'minimum_score': 15}
}

# Define backgrounds
backgrounds = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit', 'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']

# Define function for rolling ability scores
def roll_ability_score():
    dice_rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(dice_rolls, reverse=True)[:3])

# Generate random character with ability scores and class
race = random.choice(races)
background = random.choice(backgrounds)
level = 1
ability_scores = [roll_ability_score() for _ in range(6)]
highest_score = max(ability_scores)

# Filter out classes that the character is not eligible for
possible_classes = []
for class_name, class_data in classes.items():
    if class_data['required_score'] in ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']:
        if class_data['required_score'] == 'STR' and ability_scores[0] >= class_data['minimum_score']:
            possible_classes.append(class_name)
        elif class_data['required_score'] == 'DEX' and ability_scores[1] >= class_data['minimum_score']:
            possible_classes.append(class_name)
        elif class_data['required_score'] == 'CON' and ability_scores[2] >= class_data['minimum_score']:
            possible_classes.append(class_name)
        elif class_data['required_score'] == 'INT' and ability_scores[3] >= class_data['minimum_score']:
            possible_classes.append(class_name)
        elif class_data['required_score'] == 'WIS' and ability_scores[4] >= class_data['minimum_score']:
            possible_classes.append(class_name)
        elif class_data['required_score'] == 'CHA' and ability_scores[5] >= class_data['minimum_score']:
            possible_classes.append(class_name)

# If there are eligible classes, randomly choose one, otherwise set class to Commoner
if possible_classes:
    class_ = random.choice(possible_classes)
else:
    class_ = 'Commoner'

# Print character information
print('Race:', race)
print('Class:', class_)
print('Level:', level)
print('Background:', background)
print('Ability Scores:')
print(f"STR: {ability_scores[0]}")
print(f"DEX: {ability_scores[1]}")
print(f"CON: {ability_scores[2]}")
print(f"INT: {ability_scores[3]}")
print(f"WIS: {ability_scores[4]}")
print(f"CHA: {ability_scores[5]}")
print(f" ")
