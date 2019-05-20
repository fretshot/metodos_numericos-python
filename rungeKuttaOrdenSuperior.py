import math

def rungeKuttaOrdenSuperior():

    print("\n\tRunge - Kutta Orden Superior\n")

    y0 = 1.1
    yPrim0 =  1.2
    h = 0.2
    t0 = 0

    k1 = (h * yPrim0)
    m1 = h * funcion(y0, yPrim0, t0)
    k2 = h * (yPrim0 + m1)
    m2 = h * funcion((y0+k1), (yPrim0+m1), (t0+h))
    y1 = y0 + ((k1+k2)/2)
    yPrim1 = yPrim0 + ((m1+m2)/2)
    
    print("k1 = ",f'{k1:.9f}')
    print("m1 = ",f'{m1:.9f}')
    print("k2 = ",f'{k2:.9f}')
    print("m2 = ",f'{m2:.9f}')
    print("y1 = ",f'{y1:.9f}')
    print("yPrim1 = ",f'{yPrim1:.9f}')

    print("\n")

    h = 0.2
    t1 = t0 + h

    k1 = (h * yPrim1)
    m1 = h * funcion(y1, yPrim1, t1)
    k2 = h * (yPrim1 + m1)
    m2 = h * funcion((y1+k1), (yPrim1+m1), (t1+h))
    y2 = y1 + ((k1+k2)/2)
    yPrim2 = yPrim1 + ((m1+m2)/2)
    
    print("k1 = ",f'{k1:.9f}')
    print("m1 = ",f'{m1:.9f}')
    print("k2 = ",f'{k2:.9f}')
    print("m2 = ",f'{m2:.9f}')
    print("y2 = ",f'{y2:.9f}')
    print("yPrim2 = ",f'{yPrim2:.9f}')


def funcion(y, yPrim, t):
    yx = (2*yPrim*t) - y
    #yx = ((2*yPrim*math.tan(t))-(y*math.log(t))) / 2
    return yx

rungeKuttaOrdenSuperior()