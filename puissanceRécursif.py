#!/usr/bin/python3
#coding: utf-8


def power(x, y):
  if y == 0:
        return 1
  else:
        return x * power(x, y-1)


try:
  x = int(input("Quel est le nombre de base : "))
  y = int(input("Quelle est la puissance : "))
  print (x, "^", y, "=", power(x,y))
except:
  print(“Veuillez saisir un nombre.”)


--------------------------------------------------------------------- Résultat --------------------------------------------------------------------------------
Quel est le nombre de base : 10
Quelle est la puissance : 3
10 ^ 3 = 1000