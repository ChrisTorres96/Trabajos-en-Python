# Las funciones que hemos hecho las podemos agregar a una clase como metodos.
# Para agregar un metodo a una clase lo podemos hacer asi: 

class Time(object):
    def print_time(self):  # Se agrega asi porque el primer parametro es llamado 'self', se ve mas elegante
        print ('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds
    # Convierte Integers a Times
    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60) # rellama a divmod divida el primer argumento por el segundo y retorna el coeficiente y el remanente como una tupla
        time.hour, time.minute = divmod(minutes, 60)
        return time
    def increment(self, seconds):   # Version metodo increment tipo funcion pura
        seconds += self.time_to_int()
        return int_to_time(seconds)
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int() #Este es mas complicado porque toma dos objetos Time como parametros. En este caso es convencional llamar al 1er
                                                          #parametro 'self' y al 2do parametro 'other
    
    """El metodo init(abre. de 'inicializacion') es un metodo especial que es invocado cuando un objeto es instanciado. Su nombre
    completo es __init__ (2 guiones bajos, seguido por init, luego 2 guiones bajos mas). Un metodo init por la clase Time se ve asi:"""
    
    def __init__(self, hour=0, minute=0, second=0): #
        self.hour = hour
        self.minute = minute
        self.second = second
    
    # Funcion que valida que un objeto Time tiene invariantes es decir errores como que aparezca un numero mayor de 60 para el parametro de minutos, etc.
    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0 or self.hour > 12:
            return 'Error de horario'
        if self.minute >= 60 or self.second >= 60:
            return 'Error de horario'
        return True
    
    """ __str__ es un metodo especial como __init__, se supone que retorna una representacion string de un objeto.
    Por ejemplo, aqui esta metodo str para objetos Time: """
    def __str__(self):
        return ('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
    
    """Por definir otros metodos especiales, puedes especificar el comportamiento de operadores en tipos definidos por el usuario. Ejemplo, si defines un metodo llamado
    __add__ para la clase Time, puedes usar el operador + en objetos Time. Aqui esta como la definicion podria lucir:
    
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)"""
    
    def __add__(self, other):   # Version mejorada de __add__ que checa el tipo de 'other e invoca entre add_time o increment:
        if isinstance(other, Time): # isinstance toma un valor y una clase objeto, y retorna True si el valor es una instancia de la clase.
            return self.add_time(other)
        else:
            return self.increment(other) # Si el valor de other es un numero e invoca increment
    
    def add_time(self, other): # Metodo que suma dos objetos Time
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def increment(self, seconds): # Metodo que incrementa la cantidad de segundos (la actualiza)
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def __radd__(self, other): # Funciona para 'sumar lado-derecho'.Este metodo es invocado cuando un objeto Time aparece en el lado derecho del operador +.
        return self.__add__(other)
    
        
# Movemos las funciones dentro de la clase y se convierten en metodos