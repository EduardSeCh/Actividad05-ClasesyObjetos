import math

def distancia_euclidiana(x1,y1,x2,y2):
    #Formula distancia entre dos puntos
    """Parámetros:
	x1 -- origen_x
	y1 -- origen_y
	x2 -- destino_x
	y2 -- destino_y"""
    result = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return result

def puntoMasCercano(puntos:list)->list:
    resultado = []
    for punto_i in puntos:
        x1 = punto_i[0]
        y1 = punto_i[1]
        min = 1000
        cercano = (0,0)
        for punto_j in puntos:
            if punto_i != punto_j:
                x2 = punto_j[0]
                y2 = punto_j[1]
                d = distancia_euclidiana(x1,y1,x2,y2)
                if d < min:
                    min = d
                    cercano = (x2,y2)
        resultado.append((punto_i,cercano))
    return resultado