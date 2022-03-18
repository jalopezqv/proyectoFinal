"""
Vista de inicio
"""

from tkinter import *
from .vot import *

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from source.inicio import *

def inicio():

    # ------------ window -----------
    
    inicio = Tk()
    inicio.title('PAGINA PRINCIPAL')
    inicio.geometry('750x550')

    # --------- connections ----------

    def s_votacion():
        inicio.destroy()
        # establecer estado de botones en la vista principal de votacion
        voting_section(NORMAL, NORMAL)

    # ---------- buttons ------------

    votar = Button(inicio, text='VOTAR', command=s_votacion)
    votar.pack()
    inicio.mainloop()
