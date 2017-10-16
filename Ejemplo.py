#class Empresa(type):
#	instances = dict()
#class Departamento(Empresa):
class Puesto(type):#Empresa):
    instances = dict()
    def __call__(cls, *args, **kwargs):
        if cls.__name__ not in Puesto.instances:
            Puesto.instances[cls.__name__]= type.__call__(cls, *args, **kwargs)
            return Puesto.instances[cls.__name__]
    #_instance = None
    #def __new__(class_, *args, **kwargs):
        #if not isinstance(class_._instance, class_):
         #   class_._instance = object.__new__(class_, *args, **kwargs)
        #return class_._instance

class Empleado(object): #object
    __metaclass__= Puesto



inst0 = Empleado()
inst1 = Empleado()
print(id(inst1) == id(inst0))
