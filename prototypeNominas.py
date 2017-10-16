from pypattyrn.creational.prototype import Prototype


class Nomina(Prototype):
    def __init__(self, nombre, apmaterno, appaterno, numero, salario):
        self.nombre = nombre
        self.apmaterno = apmaterno
        self.appaterno = appaterno
        self.numero = numero
        self.salario = salario
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

