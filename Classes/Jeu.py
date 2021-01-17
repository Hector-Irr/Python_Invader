"""
C'est le programme principal
@author: Hector Irrmann
Created on Fri Dec 18 2020
To Do: Mouvement, tirs, score, vies, menu, enemi bonus, formes complexes
"""

#On appelle toutes les classes nécessaire et tkinter
from tkinter import *
from Joueur import Joueur 
from Alien import Alien 
from Obus import Obus
from Mur import Mur 




class Jeu(): 

    def __init__(self): 
        self.tk=Tk()
        self.tk.title('Space Invaders')
        self.x=620 
        self.y=795

        self.x0=0
        self.y0=0

#On écrit "Space Invaders" en gros sur le haut de la fenêtre        
        self.titre=Label(self.tk,text="Space Invaders",font=("Helvetica",30)) .grid(row=1,column=2)

#On affiche le score et les vies
        self.score=Label(self.tk,text="Score: ",font=("Helvetica",15)).grid(row=2,column=3, sticky='NSWE')
        self.vie=Label(self.tk,text="Lives: ",font=("Helvetica",15)).grid(row=2,column=1,sticky='W')

#On crée le canvas        
        self.canvas=Canvas(self.tk,width=1200,height=800,bg='black') 
        self.img=PhotoImage(file='../Images/terre.gif') 
        self.canvas.create_image(600,400,image=self.img) 
        self.canvas.grid(row=3, columnspan=5,rowspan=5)

#on créer les boutons quit et start ( le bouton menu se content de quitter la page, je n'ai pas eu le temps de l'améliorer)
        self.menu=Button(self.tk,text="Menu",font=("Helvetica",15),command=self.tk.destroy,bg='royal blue',height=2,width=5)
        self.menu.grid(row=3,column=6,sticky='NE')

        self.quit=Button(self.tk,text="Quit",font=("Helvetica",15),command=self.tk.destroy,bg='firebrick1',height=2,width=5)
        self.quit.grid(row=3,column=6,sticky='S')

        self.start=Button(self.tk,text="Start",font=("Helvetica",50),command=self.lancement,bg='forest green',height=2,width=5)
        self.start.grid(row=5,column=2,sticky='NSWE') 

#on appelle les différentes classes
        self.j=Joueur(self.x,self.y)
        self.a=Alien(self.y0,self.x0,self.canvas) 
        self.m=Mur()
        self.o=Obus()

#on crée et on affiche des variable score et vie
        self.affiscore=StringVar()
        self.affiscore.set(self.j.score())
        self.scoreaffi=Label(self.tk,textvariable=self.affiscore,font=("Helvetica",15))
        self.scoreaffi.grid(row=2,column=3,sticky='E')

        self.vie=StringVar()
        self.vie.set(self.j.vie())
        self.vieaffi=Label(self.tk,textvariable=self.vie,font=("Helvetica",15))
        self.vieaffi.grid(row=2,column=1,)
         

         
       
   
    def debut(self):  
        self.tk.mainloop() 


    def lancement(self): 

        self.start.grid_forget()

        self.j.image(self.canvas) 

        self.a.creer() 

        self.m.image(self.canvas) 

   

    
    
   
        
 

   
 
jouer=Jeu()
jouer.debut()