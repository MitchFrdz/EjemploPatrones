#class Empresa(object):

#class Departamento(Empresa):

class Puesto(object):#Empresa):
    #instances = {}
    #def __call__(cls, *args, **kwargs):
        #if cls not in cls._instances:
            #cls._instances[cls]= super(Puesto, cls).__call__(*args, **kwargs)
            #return cls._instances[cls]
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance   
    
class Empleado(Puesto): #object
   # __metaclass__= Puesto
        

    
x = Puesto('DFGS345')
print (x)
y = Puesto('DFGS345')
print (y)
z = Puesto('DFVE345')
print (z)
print(x)
print(y)
print(z)
