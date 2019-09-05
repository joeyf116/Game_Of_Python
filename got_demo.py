from pprint import pprint
from characters import characters

def num_of_names_start_with(a):
    num = []
    for character in characters:
        if character['name'].startswith(a) == True:
            num.append(character['name'])
    print(len(num))

num_of_names_start_with("A")
num_of_names_start_with('Z')

def dead_people():
    num = []
    for character in characters:
        if character['died'] != "":
            num.append(character['died'])
    print(len(num))

dead_people()
most_titles = 0
for person in characters:
    num_titles = len(person['titles'])
    if num_titles > most_titles:
        most_titles = num_titles
for person in characters:
    num_titles = len(person['titles'])
    if num_titles == most_titles:
        print("%s has %d titles" % (person['name'], most_titles))
    





