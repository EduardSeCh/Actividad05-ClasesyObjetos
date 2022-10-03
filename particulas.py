from particula import Particula

class Particulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self,particula:Particula):
        self.__particulas.append(particula)
    
    def agregar_inicio(self,particula:Particula):
        self.__particulas.insert(0,particula)
        
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
            
preuba = Particula(1,2,3,4,5,6,7,8,9)
prueba2 = Particula(10,20,30,40,50,60,70,80,90)
prueba3 = Particula(65,7,4,8,3,9,1,78,70)
particulas = Particulas()
particulas.agregar_inicio(preuba)
particulas.agregar_final(prueba3)
particulas.agregar_inicio(prueba2)
particulas.mostrar()