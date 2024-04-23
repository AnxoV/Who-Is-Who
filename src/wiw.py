from os import getcwd
from os.path import join
from pyswip import Prolog
from random import choice

prolog = Prolog()

PATH = getcwd()
prolog.consult(join(PATH, "src/wiw.pl"))

characters = set()
properties = set()

def query(query_string):
    return list(prolog.query(query_string))

def character_has_property(character, property):
    character_properties = query(f"character({character}, Properties)")[0]
    properties = character_properties["Properties"]

    if property in properties:
        return True
    
    return False

characters_query = query("character(Name, Properties)")

for character in characters_query:
    name = character["Name"]
    character_properties = character["Properties"]

    characters.add(name)
    properties.update(character_properties)

characters = list(characters)
properties = list(properties)
known_properties = dict()
excluyent_properties = {
    "man": "woman", "woman": "man",
    "short_hair": "long_hair", "long_hair": "short_hair",
    "small_nose": "big_nose", "big_nose": "small_nose",
    "small_mouth": "big_mouth", "big_mouth": "small_nose",
    "brown_eyes": "blue_eyes", "blue_eyes": "brown_eyes"
}

print("Piensa en uno de los personajes :D")
#input("Presiona [ENTER] para continuar ")

while True:
    random_property = choice(properties)
    properties.remove(random_property)

    if random_property in excluyent_properties.keys():
        excluyent_property = excluyent_properties[random_property]
        print(excluyent_property)
        properties.remove(excluyent_property)

    question = input(f"¿{random_property}? (s/n): ")
    if question.lower() == "s":
        question = True
    else:
        question = False

    known_properties[random_property] = question

    characters = [character for character in characters if question == character_has_property(character, random_property)]

    if len(characters) == 1:
        print("Gané :p, personaje:", characters[0])
        break
    elif len(characters) == 0:
        print("No me engañes :c")
        break