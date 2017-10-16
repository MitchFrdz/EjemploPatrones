#class Empresa(type):
#	instances = dict()
#class Departamento(Empresa):
class Registro_Empleado(type):
    instances = dict()
    def __call__(cls, *args, **kwargs):
        if cls.__name__ not in Puesto.instances:
            Puesto.instances[cls.__name__]= type.__call__(cls, *args, **kwargs)
            return Puesto.instances[cls.__name__]

class Empleado(object):
    __metaclass__= Registro_Empleado



inst0 = Empleado()
inst1 = Empleado()
print(id(inst1) == id(inst0))
print (inst0)
