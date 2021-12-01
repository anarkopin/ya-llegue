class Persona():
    def __init__(self):
        self.dni = 72863971
    
    def mensaje(self):
        print("Saludos desde la clase persona")

class Obrero(Persona):
    def __init__(self):
        self.__especialista = 1

    """def mensaje(self):
        print("Saludos desde la clase obrero")"""


obrero_planta = Obrero()
obrero_planta.mensaje()