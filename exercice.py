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

"""def draw_tree(branch_len = 70, pen_size = 7, angle = 35): 
    turtle.pencolor("green")
    turtle.left(90)
    turtle.pensize(pen_size)
    turtle.forward(branch_len)
    branch_len -= 10
    pen_size -= 1

    def left(angle, branch, branch_distance):
        if branch > 0 and branch_distance > 0: 
            turtle.pendown()
            turtle.pensize(branch)
            turtle.left(angle)
            turtle.forward(branch_distance)
            left(angle-5, branch-1, branch_distance-10)

    def right(angle, branch, branch_distance):
        if branch > 0 and branch_distance > 0: 
            turtle.pendown()
            turtle.pensize(branch)
            turtle.right(angle)
            turtle.forward(branch_distance)
            right(angle-5, branch-1, branch_distance-10)

    def back_left(angle, branch, branch_distance):
        turtle.penup()
        if branch > 0:
            turtle.backward(branch_distance)
            turtle.right(angle)
            back_left(angle+5, branch-1, branch_distance+10)
            

    def back_right(angle, branch, branch_distance):
        turtle.penup()
        if branch > 0:
            turtle.backward(branch_distance)
            turtle.left(angle)
            back_right(angle+5, branch-1, branch_distance+10)

    def other_side_left(angle_min, level, len_min):
        for number in range(1, level):
            left(angle_min+5*(number-1), number, len_min+10*(number-1))
            if number == 1:
                back_left(angle_min, 1, len_min)
                back_right(angle_min+5*number, 1, len_min+10*number)
            elif number > 1:
                back_left(angle_min, 1, len_min)
                for occurence in range(1, number):
                    right(angle_min+5*(occurence-1), occurence, len_min+10*(occurence-1))
                    back_right(angle_min, occurence, len_min)
                    back_left(angle_min+5*occurence, 1, len_min+10*occurence)
                back_right(angle_min+5*number, 1, len_min+10*number)

    def other_side_right(angle_min, level, len_min):
        for number in range(1, level):
            right(angle_min+5*(number-1), number, len_min+10*(number-1))
            if number == 1:
                back_right(angle_min, 1, len_min)
                back_left(angle_min+5*number, 1, len_min+10*number)
            elif number > 1:
                back_right(angle_min, 1, len_min)
                for occurence in range(1, number):
                    left(angle_min+5*(occurence-1), occurence, len_min+10*(occurence-1))
                    back_left(angle_min, occurence, len_min)
                    back_right(angle_min+5*occurence, 1, len_min+10*occurence)
                back_left(angle_min+5*number, 1, len_min+10*number)

            
    def side_left(angle, pen_size, branch_len):
        left(angle, pen_size, branch_len)
        angle_left = angle_min = angle - (pen_size-1)*5
        len_left = len_min = branch_len - (pen_size-1)*10
        back_left(angle_min, 1, len_min)
        for level in range(1, pen_size):
            right(angle_left, level, len_left)
            if level == 1:
                back_right(angle_min, level, len_min)
                angle_left += 5
                len_left += 10
                back_left(angle_left, 1, len_left)
            elif level > 1:
                back_right(angle_min, 1, len_min)
                other_side_left(angle_min, level, len_min)
                angle_left += 5
                len_left += 10
                back_left(angle_left, 1, len_left)

    def side_right(angle, pen_size, branch_len):
        right(angle, pen_size, branch_len)
        angle_right = angle_min = angle - (pen_size-1)*5
        len_right = len_min = branch_len - (pen_size-1)*10
        back_right(angle_min, 1, len_min)
        for level in range(1, pen_size):
            left(angle_right, level, len_right)
            if level == 1:
                back_left(angle_min, level, len_min)
                angle_right += 5
                len_right += 10
                back_right(angle_right, 1, len_right)
            elif level > 1:
                back_left(angle_min, 1, len_min)
                other_side_right(angle_min, level, len_min)
                angle_right += 5
                len_right += 10
                back_right(angle_right, 1, len_right)
    
    
    side_left(angle, pen_size, branch_len)
    side_right(angle, pen_size, branch_len)"""


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

