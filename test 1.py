#fichier python qui fait un convertisseur de miles à kilomètres.

import tkinter as tk
#from tkinter import ttk => devient inutile par rapport a ttkbootstrap
import ttkbootstrap as ttk # module meilleur que tkinter pour le graphic.

def convert():
    mile_input = entry_int.get() # la méthode .get() permet d'avoir la valeur de la variable.
    km_output =  mile_input * 1.61
    output_string.set(km_output)

#créer l'instance de la fenetre
window = ttk.Window(themename = 'darkly') # le themename permet d'appliquer un style aux boutons et a la fenêtre

#modifie des paramètres de la fenêtre
window.title('Converter')

window.geometry('300x150') # longeur et largeur séparés par un x minuscule!!!

#Pour créer le titre du convertisseur
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')  # dire à qui appartient le text

# et permet de mettre des arguements pour changer la tête du text.

title_label.pack() #méthode la plus simple pour afficher le texte précédent sur la fenêtre 

#pour créer la barre ou on écrit avec le boutton pour lancer la conversion.
input_frame = ttk.Frame(master = window)

entry_int = tk.IntVar() #variable qui va prendre les valeurs à qui on a donné le droit, a spécifié dans le label utilisé

entry = ttk.Entry(master = input_frame, textvariable = entry_int) #la barre d'entrée

button = ttk.Button(master = input_frame, text = 'Convert', command = convert)

#le boutton sur lequel appuyer pour la conversion avec la commande qui répond a la fonction convert
entry.pack(side = 'left', padx = 10) #pour afficher la barre, la placer sur une position par défaut, qui met les éléments par colonnes 1 endessous de l'autre

button.pack(side = 'left') #pareil l'argument side permet d'être plus précis le padx permet de mettre de l'espace entre les deux

input_frame.pack(pady = 10)#encore et en changeant avec un padding en y de 10 px

output_string = tk.StringVar() #variable qui stock des lettres aux lieu de chiffres.

#pour afficher le résultat de la conversion.
output_label = ttk.Label(master = window,
                         text = 'Output',
                         font = ' Calibri 20',
                         textvariable = output_string) # la texte variable passe par dessus le texte donc bessoins de output_string.set('la string') pour afficher

output_label.pack(pady = 10)



#pour que la fenêtre existe.
window.mainloop()
