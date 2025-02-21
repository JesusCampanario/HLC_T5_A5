class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} años y soy {self.profesion}"
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion, grado):
        super().__init__(nombre, edad, profesion)
        self.grado = grado 
    
    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} años y estudio {self.grado}"

p = Persona("Ana", 28, "Ingeniera")
print(p.presentarse())

estudiante = Estudiante("Carlos", 22, "Estudiante", "Matemáticas")
print(estudiante.presentarse())