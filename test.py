"""
C'est le programme principal
@author: Hector Irrmann
Created on Fri Dec 18 08:10:26 2020
To Do: Mouvement, tirs, score, vies, menu, enemi bonus, formes complexes
"""

from tkinter import *
from random import *


class Joueur():
    def __init__(self,x,y):
        self.x=x
        self.y=y 

    
    def image(self,canvas):
        canvas.create_rectangle(self.x, self.y, self.x-40, self.y-20, fill='green')
        canvas.create_rectangle(self.x-10, self.y, self.x-30, self.y-40, fill='green')

    def move(self,direction,canvas):
        self.bord()

        if direction=='right':
            self.x = self.x+5
            self.image(canvas)  

        elif direction=='left': 
            self.x= self.x-5


    def bord(self): 

        if self.x >= 1200:
            self.x=1200

        elif self.x <= 40: 
            self.x=40

    def score(self):
        self.score=0


        return self.score

    def vie(self):
        self.vie=3


        return self.vie
    

 
 
class Alien(): 
    direction='right'

    def __init__(self,x,y,canvas):  
        self.x=x
        self.y=y
        self.listAlien=[]
        self.nbAlien=10
        self.canvas=canvas

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

             
    def move(self):
        #self.bord()
        self.posx=10

        if Alien.direction=='right': 
            self.posx= self.posx+10 
 
            
        elif Alien.direction=='left':    
            self.posx=self.posx-10

        for i in range(self.nbAlien): 
                #self.canvas.delete(self.listAlien[i])
                #self.canvas.move(self.listAlien[i],10,0) 

                #self.listAlien[i]=(self.image(1,self.posx+i*50+10,10)) 


                self.listAlien.append(self.image(1,self.posx+i*50,10))  
                self.listAlien.append(self.image(2,self.posx+i*50,60))  
                self.listAlien.append(self.image(3,self.posx+i*50,110))     
            

        
 

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
 

    def creer(self):
        for i in range(self.nbAlien):
            self.listAlien.append(self.image(1,10+i*50,10))
            self.listAlien.append(self.image(2,10+i*50,60))
            self.listAlien.append(self.image(3,10+i*50,110)) 


        

            



           

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






class Obus():

    def __init__(self):
        a=0

    def tirj(self):
        tirj=1


    def tira(self):
        tira=1
 



        
 

class Jeu(): 

    def __init__(self): 
        self.tk=Tk()
        self.tk.title('Space Invaders')
        self.x=620
        self.y=795

        self.x0=0
        self.y0=0

        
        self.titre=Label(self.tk,text="Space Invaders",font=("Helvetica",30)) .grid(row=1,column=2)


        self.score=Label(self.tk,text="Score: ",font=("Helvetica",15)).grid(row=2,column=3, sticky='NSWE')
        self.vie=Label(self.tk,text="Lives: ",font=("Helvetica",15)).grid(row=2,column=1,sticky='W')

         
        self.canvas=Canvas(self.tk,width=1200,height=800,bg='black') 
        self.img=PhotoImage(file='Images/terre.gif')
        self.canvas.create_image(600,400,image=self.img) 
        self.canvas.grid(row=3, columnspan=5,rowspan=5)


        self.menu=Button(self.tk,text="Menu",font=("Helvetica",15),command=self.tk.destroy,bg='royal blue',height=2,width=5)
        self.menu.grid(row=3,column=6,sticky='NE')

        self.quit=Button(self.tk,text="Quit",font=("Helvetica",15),command=self.tk.destroy,bg='firebrick1',height=2,width=5)
        self.quit.grid(row=3,column=6,sticky='S')

        self.start=Button(self.tk,text="Start",font=("Helvetica",50),command=self.lancement,bg='forest green',height=2,width=5)
        self.start.grid(row=5,column=2,sticky='NSWE') 


        self.j=Joueur(self.x,self.y)
        self.a=Alien(self.y0,self.x0,self.canvas) 
        self.m=Mur()
        self.o=Obus()


        self.affiscore=StringVar()
        self.affiscore.set(self.j.score())
        self.scoreaffi=Label(self.tk,textvariable=self.affiscore,font=("Helvetica",15))
        self.scoreaffi.grid(row=2,column=3,sticky='E')

        self.vie=StringVar()
        self.vie.set(self.j.vie())
        self.vieaffi=Label(self.tk,textvariable=self.vie,font=("Helvetica",15))
        self.vieaffi.grid(row=2,column=1,)
         

         
        #self.tk.bind("<Right>",self.j.move('right',self.canvas))   
        #self.tk.bind("<Left>",self.j.move('left,self.canvas))
        #self.tk.bind("<space>",self.o.tirj)      

       
   
    def debut(self):  
        self.tk.mainloop() 


    def lancement(self): 

        self.start.grid_forget()

        self.j.image(self.canvas) 

        self.a.creer() 

        self.m.image(self.canvas) 

        self.a.move()   

    
    
   
        
 

   
 
jouer=Jeu()
jouer.debut()


