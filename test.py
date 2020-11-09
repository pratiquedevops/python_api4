"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Salut les Zér0s !")

# On affiche le label dans la fenêtre
champ_label.pack()

def callback():
    print( "click!")

b = Button(fenetre, text="OK", command=callback)
b.pack()
def moro():
  print("c est cool les gars!! courage !!")

m=Button(fenetre, text="presserr le bouton",command=moro)
m.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

