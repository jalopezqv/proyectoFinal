"""
13/03/22
Aún no esta unido a otro modulo
"""

from tkinter import *

def voting_section():

    # window
    votacion = Tk()
    votacion.geometry('750x550')
    votacion.title('Elecciones Cali 2022')
    votacion.configure(bg='white')

    h1 = Label(votacion, text='ELECCIONES CALI 2022', bg='white', font=('helvetica', 14))

    # Buttons
    img_gob = PhotoImage(file="img/gobernacion.png")
    gobernacion = Button(votacion, image=img_gob, relief="raised", borderwidth=2)

    img_alc = PhotoImage(file="img/alcaldia.png")
    alcaldia = Button(votacion, image=img_alc, relief="raised", borderwidth=2)

    vgob_blanco = Button(votacion, text='VOTO EN BLANCO', height=2, width=28)
    valc_blanco = Button(votacion, text='VOTO EN BLANCO', height=2, width=28)
    
    
    img_salir = PhotoImage(file="img/vote.png")
    salir = Button(votacion, text='Finalizar', font=('helvetica',12), image=img_salir, compound=RIGHT)

    # llamados y ubicaciones
    h1.pack()
    h1.place(x=270, y=40)

    gobernacion.pack()
    gobernacion.place(x=75, y=100)

    alcaldia.pack()
    alcaldia.place(x=395, y=100)

    vgob_blanco.pack()
    vgob_blanco.place(x=101, y=383)

    valc_blanco.pack()
    valc_blanco.place(x=421, y=383)

    salir.pack()
    salir.place(x=311, y=470)

    votacion.mainloop()

voting_section()