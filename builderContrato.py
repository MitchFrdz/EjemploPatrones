from pypattyrn.creational.builder import Builder, Director


class Cliente(object):  # El objeto a ser construido.
    def __init__(self):
        self.Cliente = None
        self.Referencia = None
        self.Empresa = None
        self.Pedido = None
        self.Precio = None
        self.FechaInicio = None
        self.FechaTerminacion = None
    def __repr__(self):
        return '|Cliente: {0.Cliente}\n|Referencia: {0.Referencia}\n|Empresa: {0.Empresa}\n|Pedido: {0.Pedido}\n|Precio: {0.Precio}\n|Fecha de Inicio: {0.FechaInicio}\n|Fecha de Terminacion: {0.FechaTerminacion}'.format(self)


class Constructor(Builder):  # Una base para el constructor.

    def __init__(self):
        super().__init__(Cliente())  # Initialize the Builder class with a Cliente instance.
        self._register('Cliente', self._build_Cliente)  # Register the keyword 'Cliente' with the _build_Cliente method.
        self._register('Referencia', self._build_Referencia)  # Register the keyword 'Referencia' with the _build_Referencia method.
        self._register('Empresa', self._build_Empresa)
        self._register('Pedido', self._build_Pedido)
        self._register('Precio', self._build_Precio)
        self._register('FechaInicio', self._build_FechaInicio)
        self._register('FechaTerminacion', self._build_FechaTerminacion)

    def _build_Cliente(self):
        pass
    def _build_Referencia(self):
        pass
    def _build_Empresa(self):
        pass 
    def _build_Pedido(Self):
        pass
    def build_Precio(self):
        pass
    def build_FechaInicio(self):
        pass
    def build_FechaTerminacion(self):
        pass
"////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
class Contrato(Constructor):  # una clase concreta Constructor para construir el contrato

    def _build_Cliente(self):
        self.constructed_object.Cliente = 'Jesus Andres Ramirez Valenzuela'  # Darle valor al atributo cliente.

    def _build_Referencia(self):
        self.constructed_object.Referencia = '1247851247'  # Darle valor al atributo Referencia

    def _build_Empresa(self):
        self.constructed_object.Empresa = 'Manpower'  # Darle valor al atributo empresa
        
    def _build_Pedido(self):
        self.constructed_object.Pedido = 'Formularios'

    def _build_Precio(self):
        self.constructed_object.Precio = 8000

    def _build_FechaInicio(self):
        self.constructed_object.FechaInicio = "11/octubre/2017"

    def _build_FechaTerminacion(self):
        self.constructed_object.FechaTerminacion = "11/Noviembre/2017"

class Director(Director):  # Una clase Directi para administrar la construccion del contrato.

    def construct(self):
        self.builder.build('Cliente')  # Construyela parte Cliente  usando la palabra clave 'Cliente'
        self.builder.build('Referencia')  # Construye la Referencia usando la palabra clave 'Referencia'
        self.builder.build('Empresa')
        self.builder.build('Pedido')
        self.builder.build('Precio')
        self.builder.build('FechaInicio')
        self.builder.build('FechaTerminacion')


Construir = Director()

Construir.builder = Contrato()  # Utiliza el constructor.
Construir.construct()  # Construye el contrato.
house = Construir.get_constructed_object()  # Toma el objeto construido.
print(repr(house))    #Imprime el objeto


