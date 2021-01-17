"""
C'est le programme qui créer les murs en début de partie
@author: Hector Irrmann
Created on Fri Dec 18 08:10:26 2020
To Do: peut être améliorer le placement des blocs
"""

from tkinter import *


class Mur():
#Pas vraiment besoin de def  __init__(self) vu que j'ai posé les murs à la main

    def image(self,canvas):
        #On fait tous les murs un par un par colonne de trois
        canvas.create_rectangle(100,500,150,550,fill='gray')
        canvas.create_rectangle(100,550,150,600,fill='gray') 
        canvas.create_rectangle(100,600,150,650,fill='gray')

        canvas.create_rectangle(150,500,200,550,fill='gray') 
        canvas.create_rectangle(150,550,200,600,fill='gray') 
        canvas.create_rectangle(150,600,200,650,fill='gray') 

        canvas.create_rectangle(200,500,250,550,fill='gray') 
        canvas.create_rectangle(200,550,250,600,fill='gray') 
        canvas.create_rectangle(200,600,250,650,fill='gray')  

        canvas.create_rectangle(250,500,300,550,fill='gray') 
        canvas.create_rectangle(250,550,300,600,fill='gray')  
        canvas.create_rectangle(250,600,300,650,fill='gray')



        canvas.create_rectangle(500,500,550,550,fill='gray') 
        canvas.create_rectangle(500,550,550,600,fill='gray')    
        canvas.create_rectangle(500,600,550,650,fill='gray') 

        canvas.create_rectangle(550,500,600,550,fill='gray') 
        canvas.create_rectangle(550,550,600,600,fill='gray')    
        canvas.create_rectangle(550,600,600,650,fill='gray')

        canvas.create_rectangle(600,500,650,550,fill='gray') 
        canvas.create_rectangle(600,550,650,600,fill='gray')    
        canvas.create_rectangle(600,600,650,650,fill='gray')

        canvas.create_rectangle(650,500,700,550,fill='gray')
        canvas.create_rectangle(650,550,700,600,fill='gray')
        canvas.create_rectangle(650,600,700,650,fill='gray')



        canvas.create_rectangle(900,500,950,550,fill='gray')
        canvas.create_rectangle(900,550,950,600,fill='gray')    
        canvas.create_rectangle(900,600,950,650,fill='gray')

        canvas.create_rectangle(950,500,1000,550,fill='gray')
        canvas.create_rectangle(950,550,1000,600,fill='gray')   
        canvas.create_rectangle(950,600,1000,650,fill='gray')

        canvas.create_rectangle(1000,500,1050,550,fill='gray')
        canvas.create_rectangle(1000,550,1050,600,fill='gray')   
        canvas.create_rectangle(1000,600,1050,650,fill='gray')

        canvas.create_rectangle(1050,500,1100,550,fill='gray')
        canvas.create_rectangle(1050,550,1100,600,fill='gray') 
        canvas.create_rectangle(1050,600,1100,650,fill='gray')