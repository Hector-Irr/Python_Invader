"""
C'est le programme définissant les aliens
@author: Hector Irrmann
Created on Fri Dec 18 2020
To Do: Mouvement, tirs, enemi bonus, formes complexes
"""

from tkinter import *



class Alien(): 
    direction='right'

    def __init__(self,x,y,canvas):  
        self.x=x
        self.y=y
        self.listAlien=[]
        self.nbAlien=10
        self.canvas=canvas


#on affiche les aliens sur le canvas
    def image(self,nb,posx,posy):
        self.nb=nb
        self.posx=posx
        self.posy=posy


        if self.nb==1:
            self.canvas.create_oval(self.posx,self.posy,self.posx+40,self.posy+40,fill='red')

            
 
        elif self.nb==2:
            self.canvas.create_rectangle(self.posx+10,self.posy,self.posx+30,self.posy+40,fill='blue')
            self.canvas.create_rectangle(self.posx,self.posy+10,self.posx+40,self.posy+30,fill='blue') 

           
            
 
        elif self.nb==3:
            self.canvas.create_rectangle(self.posx,self.posy,self.posx+40,self.posy+10,fill='pink')
            self.canvas.create_rectangle(self.posx,self.posy,self.posx+10,self.posy+30,fill='pink')
            self.canvas.create_rectangle(self.posx+30,self.posy,self.posx+40,self.posy+30,fill='pink') 

#cette fonction devait permettre aux aliens de bouger mais elle ne fonctionne pas            
    def move(self):
        #self.bord()
        self.posx=10

        if Alien.direction=='right': 
            self.posx= self.posx+10 
 
            
        elif Alien.direction=='left':    
            self.posx=self.posx-10

        for i in range(self.nbAlien): 
                self.listAlien.append(self.image(1,self.posx+i*50,10))  
                self.listAlien.append(self.image(2,self.posx+i*50,60))  
                self.listAlien.append(self.image(3,self.posx+i*50,110))     
            

#cette fonction aurait dû permettre d'empêcher les aliens de sortir de l'écran mais elle ne marche pas
    def bord(self):
    
        if self.x >=450:
            self.x=450
            self.y=self.y+40
            if self.y >=620:
                perdu=True
            Alien.direction='left'
 
        elif self.x <=0:
            self.x=0 
            self.y=self.y+40
            if self.y >=620:
                perdu=True
            Alien.direction='right'
 
#On crée les aliens au lancement
    def creer(self):
        for i in range(self.nbAlien):
            self.listAlien.append(self.image(1,10+i*50,10))
            self.listAlien.append(self.image(2,10+i*50,60))
            self.listAlien.append(self.image(3,10+i*50,110)) 

