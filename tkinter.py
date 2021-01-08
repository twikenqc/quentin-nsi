from tkinter import *
fenetre = Tk()

label=Label(fenetre,text="hello,world")
label.pack()
print(hex(31))

Bouton_sortie=Button(fenetre,text="quitter",command=fenetre.quit)
Bouton_sortie.pack()
fenetre.mainloop()
