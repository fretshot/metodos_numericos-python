import math

def rungeKutta2doOrden():

    print("\n\tRunge - Kutta 2do Orden\n")

    y0 = 3
    h = 0.2
    t0 = 0

    k1 = h * funcion(y0,t0)
    k2 = h * funcion((y0+k1),(t0+h))
    y1 = y0 + ((k1+k2)/2)
    
    print("k1 = ",f'{k1:.8f}')
    print("k2 = ",f'{k2:.8f}')
    print("y1 = ",f'{y1:.8f}')

    print("\n")

    h = 0.2
    t1 = t0 + h

    k1 = h * funcion(y1,t1)
    k2 = h * funcion((y1+k1),(t1+h))
    y2 = y1 + ((k1+k2)/2)
    
    print("k1 = ",f'{k1:.8f}')
    print("k2 = ",f'{k2:.8f}')
    print("y2 = ",f'{y2:.8f}')

def funcion(y,t):
    yx = (-y * math.cos(t)) / (1 - math.sin(t))
    return yx

rungeKutta2doOrden()