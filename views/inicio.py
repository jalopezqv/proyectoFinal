"""
Vista de inicio
"""

import opcode
from tkinter import *
from .vot import *

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from source.inicio import *

def inicio():

    # ------------ window -----------
    
    inicio = Tk()
    inicio.title('Inicio')
    inicio.configure(bg='white')

    ancho_ventana = 750
    alto_ventana  = 550

    x_ventana = inicio.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = inicio.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    inicio.geometry(posicion)

    # --------- connections ----------

    def s_votacion():
        cedula_votante = txt_cedula_identidad.get()
        sexo_votante   = opcion.get()
        if validar_votante(cedula_votante):
            inicio.destroy()
            show_votacion(cedula_votante, sexo_votante)

        txt_cedula_identidad.delete(0,END)
        opcion.set(None)

      
    # ---------- Headboard -----------

    # img elecciones 2022
    img1 = PhotoImage(master=inicio, file='img/elecciones2.png')
    lbl_img1 = Label(inicio, image=img1, bg='white')

    h1 = Label(inicio, text='ELECCIONES CALI 2022', bg='white', font=('helvetica', 14))

    # ---------- Entrys ------------
    txt_cedula_identidad = Entry(inicio, width=10, text='Ingrese su cedula de identificacion ... ')
    
    # ---------- RadioButtons ------------
    opcion = IntVar()
    rbt_masculino = Radiobutton(inicio, text='Masculino', variable=opcion, value=1)
    rbt_femenino  = Radiobutton(inicio, text='Femenino',  variable=opcion, value=2)

    # ---------- buttons ------------
    btn_votar = Button(inicio, text='VOTAR', command=s_votacion)

    # ----- llamados y ubicaciones -----

    h1.pack()
    h1.place(x=270, y=40)

    lbl_img1.pack()
    lbl_img1.place(x=90, y=7)


    txt_cedula_identidad.pack()
    txt_cedula_identidad.place(x=375, y= 270)

    rbt_masculino.pack()
    rbt_masculino.place(x=450, y=270)
    rbt_femenino.pack()
    rbt_femenino.place(x=550, y=270)

    btn_votar.pack()
    btn_votar.place(x=375, y=300)
    inicio.mainloop()
