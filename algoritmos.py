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