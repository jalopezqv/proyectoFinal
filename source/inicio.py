"""
Funcionalidad vista de inicio
"""

from operator import truediv
from tkinter import *
from tkinter import messagebox

lista_votantes = []

# validar si el votante ya ejercio su voto
def validar_votante(cedula):
        
    if cedula in lista_votantes:
        messagebox.showinfo(message="El documento ingresado ya se encuentra registrado, tenga en cuenta que solo puede votar 1 vez", title="ERROR")
        return False
    return True

# conectar con vista de votacion y configurar el estado de los botones 
def show_votacion(cedula, sexo_votante):
    try:
        import votacion
    except ImportError:
        import sys
        votacion = sys.modules[__package__ + '.votacion']

    datos_votante = [cedula, sexo_votante]
    lista_votantes.append(datos_votante)

    votacion.func_states(NORMAL,3)