#from historial_medico import HistorialMedico
#from conexion10 import BaseDatos
import re

class Mascota:
    def __init__(
            self,
            codigo_mascota: int = None,
            nombre: str = None,
            especie: str = None,
            genero: str = None, 
            raza: str = None,
            edad: float = None,
            peso: float = None,
            usuario: int = None,
            historial_medico= None
            ):
        self.__codigo_mascota = codigo_mascota        
        self.__nombre = nombre
        self.__especie = especie
        self.__genero = genero
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__usuario = usuario
        self.__historial_medico = historial_medico if historial_medico is not None else []