class Trabajador:
    def __init__(self, nombre, edad, trabajo, empresa):
        self.nombre = nombre
        self.edad = edad
        self.trabajo = trabajo
        self.empresa = empresa

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} , tengo {self.edad} años, soy {self.trabajo} y trabajo en {self.empresa}")
    
t = Trabajador("Jesús", 19,"informatico","Mediamarkt")
print(t)
jesus = (t.presentarse())