#!/usr/bin/env python
# -*- coding: utf-8 -*-

def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = list(map(str, input('Entrez dix valeurs: ').split()))
        values = values[:10]

    return sorted(values)

def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = list(map(str, input('Entrez deux mots: ').split()))
    word1 , word2 = words[0] , words[1]
    return sorted(word1) == sorted(word2)


def contains_doubles(items: list) -> bool:
    return False if len(items) == len(set(items)) else True


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    averages = []
    names = []
    for student, tests in student_grades.items() :
        average = sum(tests) / len(tests)
        averages.append(average)
        names.append(student)
    best_average = max(averages)
    best_student = names[averages.index(best_average)]   

    return {best_student : best_average}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    letter_appearence = {}
    letters = set(sentence)
    characters = list(sentence)
    for letter in letters :
        appearence = characters.count(letter)
        """if appearence > 5 : #Erreur dans le fichier test pour cette contrainte...
            with5_appearence[letter] = appearence"""
        letter_appearence[letter] = appearence
    letter_appearence = dict(sorted(letter_appearence.items(), key=lambda index: index[1], reverse=True))

    return letter_appearence


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recipes = {}
    recipe = str(input("Entrez le nom d'une recette: "))
    ingredients = list(map(str, input('Entrez les ingrédients de cette recette: ').split()))
    recipes[recipe] = set(ingredients)

    return recipes

def print_recipe(recipes) -> None: # Recipes déjà dictionnaire ....
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recipe_choice = input('Choisissez une recette: ')
    if recipe_choice in recipes :
        print(str(recipes[recipe_choice]))
    else :
        print(f"La recette {recipe_choice} n'est pas disponible")


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
