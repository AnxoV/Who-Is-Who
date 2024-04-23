from os import getcwd
from os.path import join
from pyswip import Prolog
from random import choice


class bidict(dict):
    def __init__(self, *args, **kwargs):
        super(bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.setdefault(value, []).append(key)

    def __setitem__(self, key, value):
        if key in self:
            self.inverse[self[key]].remove(key)
        super(bidict, self).__setitem__(key, value)
        self.inverse.setdefault(value, []).append(key)

    def __delitem__(self, key):
        self.inverse.setdefault(self[key], []).remove(key)
        if self[key] in self.inverse and not self.inverse[self[key]]:
            del self.inverse[self[key]]
        super(bidict, self).__delitem__(key)


def query(query_string):
    return list(prolog.query(query_string))


def character_has_property(character, property):
    character_properties = query(f"character({character}, Properties)")[0]
    properties = character_properties["Properties"]

    if property in properties:
        return True
    
    return False


prolog = Prolog()

PATH = getcwd()
prolog.consult(join(PATH, "src/wiw.pl"))

# unique_properties = set()
# possible_characters = list()
# fill both from prolog
# ask most relevant question (the feature that appears the most accross characters)
# remove excluyen features
# remove characters and features that doesn't match
# repeat until one character remains (if answered correctly)

unique_properties = dict()
possible_characters = list()

excluyent_properties = bidict({
    "man": "woman",
    "short_hair": "long_hair",
    "small_nose": "big_nose",
    "small_mouth": "big_mouth",
    "brown_eyes": "blue_eyes"
})

characters_query = query("character(Name, Properties)")

for character in characters_query:
    for property in character["Properties"]:
        if property not in unique_properties.keys():
            unique_properties[property] = 1
        else:
            unique_properties[property] += 1

    possible_characters.append(character["Name"])

unique_properties = dict(sorted(unique_properties.items(), key=lambda item: item[1]))

print("Think about a character :D")

while True:
    len_unique_properties = len(unique_properties.keys())
    random_property = list(unique_properties.keys())[len_unique_properties//2]
    
    while (question := input(f"{random_property}? (y/n): ").lower()) not in ["y", "n"]:
        print("Invalid response")

    if question == "y":
        question = True
    else:
        question = False

    del unique_properties[random_property]
    try:
        excluyent_property = excluyent_properties[random_property]
        del unique_properties[excluyent_property]
    except KeyError:
        pass
    
    possible_characters = [char for char in possible_characters if (question == character_has_property(char, random_property))]

    if len(possible_characters) == 1:
        print("I won :P, your character was:", possible_characters[0])
        break
    elif len(possible_characters) == 0:
        print("Something didn't go well :c")
        break