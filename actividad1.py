class Persona:
    def __init__(self,nombre,edad,profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def presentarse(self):
        return f"Soy {self.nombre} tengo {self.edad} años y soy {self.profesion}"
    
p = Persona("Ana", 28,"Ingeniera")
print(p.presentarse())