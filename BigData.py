
import json
from Persona import *
import os
import pathlib

class Persona:

    AGREGAR_PERSONA=1
    CONSULTAR_PERSONA=2
    SALIR=0

    def __init__(self):
        self.Persona=[]

    def __del__(self):
        pass.Persona=[] 
  
    @property
    def Persona(self)
        return self._Persona  
    @Persona.setter
    def nombre(self,valor)
        return self._valor
    @Persona.deleter
    def Persona(self,valor)
        return self._Persona  
    
    def AGREGAR_PERSONA(self,ruta):
        pass.Persona=[] 
    def CONSULTAR_PERSONA(self):
        pass.Persona=[]
    
    
    


    def _init_(selft, nombre='', edad='', ciudad='', fecha_nacimiento=''): 
        selft._nombre= nombre
        selft._edad= edad
        selft._ciudad= ciudad
        selft._fecha_nacimiento= fecha_nacimiento

    @property
    def nombre(self)
        return self._nombre   
    @nombre.setter
    def nombre(self,valor)
        return self._valor
    @nombre.deleter
    def nombre(self,valor)
        return self._nombre   

    @property    
    def edad(self)
        return self._edad  
    @edad.setter
    def edad(self,valor)
        return self._valor
    @edad.deleter
    def edad(self,valor)
        return self._edad  

    @property
    def ciudad(self)
        return self._ciudad  
    @ciudad.setter
    def ciudad(self,valor)
        return self._valor
    @ciudad.deleter
    def ciudad(self,valor)
        return self._ciudad 

   @property
    def fecha_nacimiento(self)
        return self._fecha_nacimiento  
    @fecha_nacimiento.setter
    def fecha_nacimiento(self,valor)
        return self._valor
    @cfecha_nacimiento.deleter
    def cfecha_nacimiento(self,valor)
        return self._fecha_nacimiento
def _str_(selft):
    ESPACIOS=25
    return f'''{"nombre: " : <{ESPACIOS}}{self.nombre}

{"edad: " : <{ESPACIOS}}{self.edad}
{"ciudad: " : <{ESPACIOS}}{self.ciudad}
{"fecha_nacimiento: " : <{ESPACIOS}}{self.fecha_nacimiento}''' 

class base_Encoder(json.JSONEncoder):
    def default(self, obj)
        if isinstance(obj,Persona)
        return {'nombre' : obj.nombre,'edad' : obj.edad,'ciudad' : obj.ciudad,'fecha_nacimiento' : obj.fecha_nacimiento}
    return json.JSONEncoder.default(self,obj)
def desde_json(diccionario):
    return Persona (diccionario['nombre'],diccionario['edad'],diccionario['ciudad'],diccionario['fecha_nacimiento'] )
{}
    