BASIQUE POUR FAIRE DU TKINTER:
-------------------------------
import tkinter a tk => import le module tkinter et l'abrege par tk

from tkinter import ttk => import le module ttk important pour les widgets


LES FENETRES :
--------------
    
window = tk.TK()  =>> créer une fenetre avec pour 'nom' window, besoin de tkinter

window.geometry('largeurxlongeur') => pour changer la taille de la fenêtre.

window.title('le nom') => pour changer le nom de la fenêtre.
window.mainloop() => permet de faire en sorte que tout s'update sur le canva. Le code apres est executé lors de

la fermeture de la fenêtre.

LES LABELS:
label = tkinter.Label(master = le parent que tu veux)  => créer un label, a besoin d'un parent, souvent window
!! il est possible de ne pas mettre master = devant car 1er argument tout le parent!!!

LES ENTREES:
-------------
entry = tk.Entry(master = le parent ) => pour créer une barre d'entrée

LES BOUTTONS :
--------------
bouton basique:
button = tk.Button(master = ton parent, text ='ce que tu veux ecrit', command = nomde ta fonction a faire) créer un boutton avec text dessus

boutton check :
check = tk.Checkbutton(master, text, variable, command, onvalue = la valeur quand check, offvalue = valeur quand pas check.)

POUR DEFINIR UNE FONCTION ET UTILISATION DES WIDGETS :
--------------------------
def nomdetafonction(): => permet de définir une fonction que tu peux ensuite utiliser avec un boutton.

!!! la fonction .pack est à utiliser comme: tonwidget.pack() afin de l'afficher sur la fenêtre sinon c'est mort...
peut rajouter dansd le parenthese side = 'left, top, bottom, right') pour positionner le widget sur la fenetre

peut utiliser la méthode du nomduwidget.get pour avoir la valeur du widget. !!! marche pas pour les labels.

nomduwidget['unargument'] = 'ceque tu veux en faire' => permet de configurer un argument de ton widget

tonwidget.config(un arguement = 'ce que tu veux') => MEME CHOSE

tonwidget.configure(un arguement = 'ce que tu veux') => MEME CHOSE

!!! possible d'utiliser ': print(nomdetonwidget.configure()) afin d'obtenir tout les arguments que tu peux configurer
sur ce widget. TREES UTILE!!! 

pass => permet de faire en, sorte que le code n'ai pas d'erreur alors qu'il manque qqchose

LES VARIABLES TKINTER ET LEUR UTILISATION: => peut utiliser .get(), est utilisé détourner pour .get sur label et bouton
-------------------------------------------
string = tk.StringVar() # utiliser textvariable = nomdelavariable string dans la définition des widgets a lier
    peu utiliser:  nomdelavariable.set(value = 'qqqchose') pour avoir un text de base pour la variable
     on peut en utilisant une stringvar avec .get obtenir la valeur d'un bouton',d'un label
     !!! cela donne une string donc le mieux c'est d'utiliser int var ou boolean var en réalité!!!

int = tk.IntVar() => donnera du type int

Boole = BooleanVar() => donnera du type boole

on peut utilise print(type(ton truc)) afin de voir a quoi correspond comme catégorie la valeure utilisée





