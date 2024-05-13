# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 23:53:06 2024

@author: ABDOULAHI FAYE
"""
import tkinter as Tk
import numpy as np

class Application:
    def __init__(self):
        """Constructeur de la fenêtre principale"""
        self.root =Tk() 
        self.root.title('Code des couleurs')
        Tk.Label(self.root, text ="Entrez la valeur de la résistance, en ohms :").grid(row =2, column =1, columnspan =3)
        self.dessineResistance()
        Tk.Button(self.root, text ='Montrer', command =self.changeCouleurs).\
        grid(row =2, column =1, columnspan =3)
        Tk.Button(self.root, text ='Quitter', command =self.root.quit).\
        grid(row =3, column =1)
        self.entree.grid(row =3, column =2) 
        self.entree = Tk.Entry(self.root, width =14).grid(row =3, column =3)
        self.cc = ['black','brown','red','orange',
                   'yellow','green','blue','purple','grey','white']
        self.root.mainloop()
    
    
    def dessineResistance(self):
        """Canevas avec un modèle de résistance à trois lignes colorées"""
        self.can.create_line(10, 50, 240, 50, width =5) 
        self.can.grid(row =1, column =1, columnspan =3, pady =5, padx =5) 
        self.can = Tk.Canvas(self.root, width=250, height =100, bg ='light blue')
        # Dessin des trois lignes colorées (noires au départ) : self.can.create_rectangle(65, 30, 185, 70, fill ='beige', width =2)
        self.ligne =[]
        # on mémorisera les trois lignes dans 1 liste
        for x in range(85,150,24):
            self.ligne.append(self.can.create_rectangle(x,30,x+12,70, fill='black',width=0))
    def changeCouleurs(self):
        """Affichage des couleurs correspondant à la valeur entrée"""
        self.v1ch = self.entree.get() 
        try:
            # cette méthode renvoie une chaîne
            v = float(self.v1ch)
        except:
            err =1
            # conversion en valeur numérique
        else:
            # erreur : entrée non numérique
            err =0
        if err ==1 or v < 10 or v > 1e11 :
            self.signaleErreur()
        else:
            li =[0]*3
            logv = int(np.log10(v))
            ordgr = 10**logv
            li[0] = int(v/ordgr)
            decim = v/ordgr - li[0]
            li[1] = int(decim*10 +.5)
            li[2]=logv-1
            for n in range(3):
                self.can.itemconfigure(self.ligne[n], fill =self.cc[li[n]])
    def signaleErreur(self):
        self.entree.configure(bg ='red')
        # colorer le fond du champ
        self.root.after(1000, self.videEntree)
    def videEntree(self):
        self.entree.configure(bg ='white') 
        self.entree.delete(0, len(self.v1ch))

# Programme principal : 
if __name__ == '__main__':
    f = Application
            