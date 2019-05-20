import math

def rungeKutta4toOrden38Simpson():

    print("\n\tRunge - Kutta 4to Orden 3/8 Simpson\n")

    y0 = 3
    h = 0.2
    t0 = 0

    k1 = h * funcion(y0,t0)
    k2 = h * funcion((y0+(k1/3)),(t0+(h/3)))
    k3 = h * funcion((y0+(k1/3)+(k2/3)),(t0+((2/3)*h)))
    k4 = h * funcion((y0+k1-k2+k3),(t0+h))
    y1 = y0 + ((1/8)*(k1+(3*k2)+(3*k3)+k4))
    
    print("k1 = ",f'{k1:.9f}')
    print("k2 = ",f'{k2:.9f}')
    print("k3 = ",f'{k3:.9f}')
    print("k4 = ",f'{k4:.9f}')
    print("y1 = ",f'{y1:.9f}')

    print("\n")

    h = 0.2
    t1 = t0 + h

    k1 = h * funcion(y1,t1)
    k2 = h * funcion((y1+(k1/3)),(t1+(h/3)))
    k3 = h * funcion((y1+(k1/3)+(k2/3)),(t1+((2/3)*h)))
    k4 = h * funcion((y1+k1-k2+k3),(t1+h))
    y2 = y1 + ((1/8)*(k1+(3*k2)+(3*k3)+k4))
    
    print("k1 = ",f'{k1:.9f}')
    print("k2 = ",f'{k2:.9f}')
    print("k3 = ",f'{k3:.9f}')
    print("k4 = ",f'{k4:.9f}')
    print("y2 = ",f'{y2:.9f}')

def funcion(y,t):
    yx = (-y * math.cos(t)) / (1 - math.sin(t))
    return yx

rungeKutta4toOrden38Simpson()