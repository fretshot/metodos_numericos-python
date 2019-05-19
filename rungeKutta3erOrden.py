import math

def rungeKutta3erOrden():

    print("\n\tRunge - Kutta 3er Orden\n")

    y0 = 3
    h = 0.2
    t0 = 0

    k1 = h * funcion(y0,t0)
    k2 = h * funcion((y0+(k1/2)),(t0+(h/2)))
    k3 = h * funcion((y0-k1+(2*k2)),(t0+h))
    y1 = y0 + ((1/6)*(k1+(4*k2)+k3))
    
    print("k1 = ",f'{k1:.9f}')
    print("k2 = ",f'{k2:.9f}')
    print("k3 = ",f'{k3:.9f}')
    print("y1 = ",f'{y1:.9f}')

    print("\n")

    h = 0.2
    t1 = t0 + h

    k1 = h * funcion(y1,t1)
    k2 = h * funcion((y1+(k1/2)),(t1+(h/2)))
    k3 = h * funcion((y1-k1+(2*k2)),(t1+h))
    y2 = y1 + ((k1+4*k2+k3)/6)
    
    print("k1 = ",f'{k1:.9f}')
    print("k2 = ",f'{k2:.9f}')
    print("k3 = ",f'{k3:.9f}')
    print("y2 = ",f'{y2:.9f}')

def funcion(y,t):
    yx = (-y * math.cos(t)) / (1 - math.sin(t))
    return yx

rungeKutta3erOrden()