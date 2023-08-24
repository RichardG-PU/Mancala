import tkinter as tk
from Puit import Puit
from Mancala import Mancala

def event_puit(id):
    # ICI l'action!!!!
    mancala = Mancala()
    puits[id].bouton.configure(text="allo")
    print(id, puits[id].label)
    status_label['text'] = puits[id].label
    if mancala.joueurDeplacement(puits[id].label) != False:
        for key, value in mancala.grille.items():
            if key == puits[id].label:
                puits[id].nbGraines = value
                print(value)
                puits[id].bouton.configure(text=str(value))

def event_reset():
    # ICI le reset
    print("Nouvelle partie!!!")

if __name__ == '__main__':
    Mancala()

    puits = []

    puits.append(Puit("1", 0, 0, 100, 300, 0))
    puits.append(Puit("G", 100, 0, 100, 100, 4))
    puits.append(Puit("H", 200, 0, 100, 100, 4))
    puits.append(Puit("I", 300, 0, 100, 100, 4))
    puits.append(Puit("J", 400, 0, 100, 100, 4))
    puits.append(Puit("K", 500, 0, 100, 100, 4))
    puits.append(Puit("L", 600, 0, 100, 100, 4))
    puits.append(Puit("2", 700, 0, 100, 300, 0))
    puits.append(Puit("A", 100, 200, 100, 100, 4))
    puits.append(Puit("B", 200, 200, 100, 100, 4))
    puits.append(Puit("C", 300, 200, 100, 100, 4))
    puits.append(Puit("D", 400, 200, 100, 100, 4))
    puits.append(Puit("E", 500, 200, 100, 100, 4))
    puits.append(Puit("F", 600, 200, 100, 100, 4))

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Projet 1 - Richard + Kenny")
    tk.Label(root, text="Mancala", font=('Arial', 25), fg='red').pack()

    play_area = tk.Frame(root, width=800, height=300, bg='white')

    for i, puit in enumerate(puits):
        if puit.nbGraines == 0 or puit.label == "1" or puit.label == "2":
            puit.bouton = tk.Button(play_area, text=str(puit.nbGraines), font=('Arial', 15))
        else:
            puit.bouton = tk.Button(play_area, text=str(puit.nbGraines), font=('Arial', 15), command=lambda id=i: event_puit(id))
        puit.bouton.place(x = puit.x, y = puit.y, width=puit.width, height=puit.height)

    status_label = tk.Label(play_area, text="Play", font=('Arial', 16), bg='white')
    status_label.place(x = 100, y = 100, width=600, height=100)

    play_area.pack(pady=10, padx=10)

    play_again_button = tk.Button(root, text='Nouvelle partie', font=('Arial', 12), command=event_reset)
    play_again_button.pack(pady=10)

    root.mainloop()

"""
 G +------+------+--<<<<<-Joueur 2----+------+------+------+ G
 R |      |G     |H     |I     |J     |K     |L     |      | R
 E |      |   4  |   4  |   4  |   4  |   4  |   4  |      | E
 N |      |      |      |      |      |      |      |      | N
 I |   0  +------+------+------+------+------+------+   0  | I
 E |      |A     |B     |C     |D     |E     |F     |      | E
 R |      |   4  |   4  |   4  |   4  |   4  |   4  |      | R
   |      |      |      |      |      |      |      |      | 
 2 +------+------+------+-Joueur 1->>>>>-----+------+------+ 1
"""