import random

# Define lists of possible values for each character attribute
races = ['Human', 'Elf', 'Dwarf', 'Halfling']
classes = ['Fighter', 'Rogue', 'Wizard', 'Cleric']
abilities = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

# Define a function to generate a random character
def generate_character():
    race = random.choice(races)
    class_ = random.choice(classes)
    abilities_scores = []
    for i in range(6):
        rolls = [random.randint(1,6) for j in range(4)]
        abilities_scores.append(sum(rolls) - min(rolls))
    abilities_dict = dict(zip(abilities, abilities_scores))
    return {'Race': race, 'Class': class_, 'Abilities': abilities_dict}

# Generate a random character and print the results
random_character = generate_character()
print('Random Character:')
print(f"Race: {random_character['Race']}")
print(f"Class: {random_character['Class']}")
print("Abilities:")
for ability, score in random_character['Abilities'].items():
    print(f"{ability}: {score}")
