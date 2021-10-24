#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import exercice_ch6
import turtle

# TODO: Définissez vos fonction ici
def ellipsoide(a, b, c, masse_volumique):
    volume = 4/3 * math.pi * a*b*c
    mass = masse_volumique * volume
    
    return volume, mass


def letter_moreAppearence(sentence):
    letter_appearence = exercice_ch6.frequence(sentence)
    sentence = letter_appearence.keys()
    letter_more_ppearence_dict = {max(sentence) : letter_appearence[max(sentence)]}
    
    return letter_more_ppearence_dict


def draw_tree(): 
    turtle.pencolor("green")
    turtle.setheading(90)
    draw_branch(70,7,35)


def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0 and pen_size > 0:
        turtle.pensize(pen_size)
        turtle.forward(branch_len)
        turtle.right(angle)
        draw_branch(branch_len-10, pen_size-1, angle-5)
        turtle.left(2*angle)
        draw_branch(branch_len-10, pen_size-1, angle-5)
        turtle.right(angle)
        turtle.backward(branch_len)


def validation_adn(adn_chain):
    if len(adn_chain) != 0:
        count = adn_chain.count('a') + adn_chain.count('t') + adn_chain.count('c') + adn_chain.count('g')
        if count == len(adn_chain):
            return True

    return False


def input_adn():
    chain = input("Entrez une valeur de chaine d'ADN : ")
    if validation_adn(chain):
        return chain
    
    print("La valeur entrée n'est pas valide")
    return(input_adn())


def frequence_sequence(chain, sequence):
    occurence = chain.count(sequence)
    percentage = len(sequence)*occurence / len(chain) *100
    if percentage == 0 or not validation_adn(chain):
        return "La séquence ne se retrouve pas dans la chaine ou n'est pas valide."

    return f"Il y a {percentage}% de {sequence}"


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    ellipsoide(2, 3, 4, 64)
    letter_moreAppearence("bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui")
    draw_tree()
    frequence_sequence('aacctgtgtcga', 'ctgt')

