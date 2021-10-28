#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
from turtle import *
import re

sys.path.insert(0, 'C:\\Users\\anner\\OneDrive\\Bureau\\intro programmation (inf1007)\\exercices\\2021a-c01-ch6-1-exercices-Anneraymond08')
from exercice_chap6 import frequence


# TODO: Définissez vos fonction ici
def ellipsoide(a=1,b=10,c=3,p=20):
    V = 4/3 * math.pi * a * b * c
    masse = p * V
    return V, masse

def draw_tree():
    setheading(90)
    color('green')
    draw_branch(70,7,35)
    done()

def draw_branch(branch_len,pen_size,angle):
    if branch_len > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len-10, pen_size - 1, angle - 5)
        left(angle*2)
        draw_branch(branch_len-10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)

def valide(sequence):
    return bool(re.match("^[actg]+$", sequence))

def saisie(type):
    value = input(f"{type}:")
    if valide(value):
        return value
    print(f"La {type} n'est pas valide.")
    return saisie(type)

def proportion(chaine, sequence):
    return chaine.count(sequence) * len(sequence) / len(chaine)

def check_dan():
    chaine = saisie("chaine")
    sequence = saisie("sequence")
    print(f"Il y a {proportion(chaine,sequence) * 100}% de {sequence}.")

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    volume, masse = ellipsoide(2,3,4,10)
    #print(volume)
    #print(masse)
    #print((lambda sentence: sorted(frequence(sentence).items(), key=lambda x: x[1])[-1][0])('Je suis une phrase eee'))
    #draw_tree()
    #print(valide('aacg'))
    #saisie("chaine")
    #print(proportion("actgaaatcgactgactg", "actg"))
    check_dan()