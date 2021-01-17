"""
C'est la classe définissant le joueur
@author: Hector Irrmann
Created on Fri Dec 18 2020
To Do: Mouvement, tirs, score, vies, 
"""




from tkinter import *


class Joueur():
    def __init__(self,x,y):
        self.x=x
        self.y=y 

#On affiche le joueur   
    def image(self,canvas):
        canvas.create_rectangle(self.x, self.y, self.x-40, self.y-20, fill='green')
        canvas.create_rectangle(self.x-10, self.y, self.x-30, self.y-40, fill='green')

#cette fonction devait permettre au joueur de se déplacer, mais elle ne fonctionne pas
    def move(self,direction,canvas):
        self.bord()

        if direction=='right':
            self.x = self.x+5
            self.image(canvas)  

        elif direction=='left': 
            self.x= self.x-5

#cette fonction devait empêcher le joueur de sortir du terrain mais elle ne fonctionne pas
    def bord(self): 

        if self.x >= 1200:
            self.x=1200

        elif self.x <= 40: 
            self.x=40

#cette fonction devait définir le score, mais comme on ne peut pas éliminer d'alien, il n'y a rien
    def score(self):
        self.score=0


        return self.score

#cette fonction devait déterminer le nombre de vie mais sans mouvement, il n'y a rien
    def vie(self):
        self.vie=3


        return self.vie
    
