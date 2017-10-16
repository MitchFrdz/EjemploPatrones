import time
from pypattyrn.creational.prototype import Prototype
class Registro_Empleado(type):
    instances = dict()
    def __call__(cls, *args, **kwargs):
        if cls.__name__ not in Puesto.instances:
            Puesto.instances[cls.__name__]= type.__call__(cls, *args, **kwargs)
            return Puesto.instances[cls.__name__]

class Empleado(object):
    __metaclass__= Registro_Empleado

class Nomina(Prototype):
    def __init__(self, nombre, apmaterno, appaterno, numero, salario, id):
        self.id=Empleado()
        self.nombre = nombre
        self.apmaterno = apmaterno
        self.appaterno = appaterno
        self.numero = numero
        self.salario = salario

class LugarO:
    def lugaroficinista(self, fHora):
        print("Entrada a Oficina :",
        fHora.entrada())

class LugarE:
    def lugarejecutivo(self, fHora):
        print"Entrada a zona v.i.p :",
        fHora.entrada())

class Oficinista:
    def entrada(self): print ("Fecha y hora de entrada: " + time.strftime("%c"))

class Ejecutivo:
    def entrada(self): print("Fecha y hora de entrada:" + time.strftime("%c"))

# Concrete factories:
class EjecutivoYHfecha:
    def registrarLugar(self): return LugarE()
    def registrarEntrada(self): return Ejecutivo()

class OficinistaYHfecha:
    def registrarLugar(self): return LugarO()
    def registrarEntrada(self): return Oficinista()

class OfficeEnvironment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.registrarLugar()
        self.ob = factory.registrarEntrada()
    def registro(self):
        self.p.interactWith(self.ob)
empleado = Nomina("Jesus", "Ramirez", "Valenzuela", 419401, 2500)

"//////////////////////////////////////////////////////////////////////////////"

clone = empleado.prototype(bono = 2000)

print ("Nomina del 01/enero/2017 al 15/enero/2017")
print("Nombre:", empleado.nombre, empleado.apmaterno, empleado.appaterno)
print("Empleado#", empleado.numero)
print("Cantidad a Pagar $", empleado.salario)
print()
"//////////////////////////////////////////////////////////////////////////////"
print("Nomina del 16/enero/2017 al 30/enero/2017")
print("Nombre:",clone.nombre, clone.apmaterno, clone.appaterno)
print("Empleado#", clone.numero)
print("Cantidad a Pagar $", clone.salario)
print("Bono Puntualidad y Asistencia $", clone.bono)
"//////////////////////////////////////////////////////////////////////////////"
clone2 = empleado.prototype(retardos = 250)
print()
print("Nomina del 1/Febrero/2017 al 15/Febrero/2017")
print("Nombre:", clone2.nombre, clone2.apmaterno, clone2.appaterno)
print("Empleado#", clone2.numero)
pago = clone2.salario - clone2.retardos
print("Cantidad a Pagar $", pago)

r1 = OfficeEnvironment(EjecutivoYHfecha())
r2 = OfficeEnvironment(OficinistaYHfecha())
r1.registro()
r2.registro()
