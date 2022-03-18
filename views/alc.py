"""
Vista votacion por alcaldia
"""

from tkinter import *

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from source.alcaldia import *

def alc():
    
    # ------------ window -----------
    global v_alc
    
    v_alc = Tk()
    v_alc.geometry('750x550')
    v_alc.title('Elecciones Cali 2022')
    v_alc.configure(bg='white')

    # ---------- Headboard -----------

    # img elecciones 2022
    img1 = PhotoImage(file='img/elecciones2.png')
    lbl_img1 = Label(v_alc, image=img1, bg='white')

    #title
    h1 = Label(v_alc, text='ALCALDÍA 2022', bg='white', font=('helvetica', 14))

    # img gobernación
    img2 = PhotoImage(file='img/alcaldia2.png')
    lbl_img2 = Label(v_alc, image=img2, bg='white')

    # -------- connections --------

    def salida():
        v_alc.destroy()
        terminar()

    # ---------- buttons ------------

    # img
    img_cand = PhotoImage(file="img/candidato.png")

    def switch(n):
        config(n, cand_1, cand_2, cand_3, cand_4, cand_5, v_blanco)

    cand_1 = Button(v_alc, text=candidatos_alc[0][0], font=('helvetica', 13), image=img_cand, compound=BOTTOM, command=lambda:switch(0))
    cand_2 = Button(v_alc, text=candidatos_alc[1][0], font=('helvetica', 13), image=img_cand, compound=BOTTOM, command=lambda:switch(1))
    cand_3 = Button(v_alc, text=candidatos_alc[2][0], font=('helvetica', 13), image=img_cand, compound=BOTTOM, command=lambda:switch(2))
    cand_4 = Button(v_alc, text=candidatos_alc[3][0], font=('helvetica', 13), image=img_cand, compound=BOTTOM, command=lambda:switch(3))
    cand_5 = Button(v_alc, text=candidatos_alc[4][0], font=('helvetica', 13), image=img_cand, compound=BOTTOM, command=lambda:switch(4))
    v_blanco = Button(v_alc, text='VOTO EN\nBLANCO', font=('helvetica', 12), width=11, height=7, command=lambda:switch(5))

    # img registraduria
    img3 = PhotoImage(file='img/registraduria.png')
    lbl_img3 = Label(v_alc, image=img3, bg='white')

    # boton finalizar
    img_salir = PhotoImage(file="img/vote.png")
    salir = Button(v_alc, text='Finalizar', font=('helvetica',12), image=img_salir, compound=RIGHT, command=salida)

    # ----- llamados y ubicaciones -----

    h1.pack()
    h1.place(x=305, y=60)

    lbl_img1.pack()
    lbl_img1.place(x=90, y=25)

    lbl_img2.pack()
    lbl_img2.place(x=550, y=7)

    cand_1.pack()
    cand_1.place(x=150, y=140)

    cand_2.pack()
    cand_2.place(x=310, y=140)

    cand_3.pack()
    cand_3.place(x=470, y=140)

    cand_4.pack()
    cand_4.place(x=150, y=300)

    cand_5.pack()
    cand_5.place(x=310, y=300)

    v_blanco.pack()
    v_blanco.place(x=470, y=300)

    lbl_img3.pack()
    lbl_img3.place(x=562, y=460)

    salir.pack()
    salir.place(x=320, y=475)

    v_alc.mainloop()
