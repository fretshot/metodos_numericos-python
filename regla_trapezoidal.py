import math

def main(n,a,b):

    h = (b - a )/ n

    i = (h/2) * (fa(a) + (2 * sumatoria(a,n,h)) + fb(b))

    print ("I = ",i)

def fa(a):
    fa = math.exp(-1 * math.pow(a,2))
    return fa

def fb(b):
    fb = math.exp(-1 * math.pow(b,2))
    return fb

def sumatoria(a,n,h):
    sumatoria = 0

    for i in range(1,n):
        sumatoria = sumatoria + (math.exp(-1 * math.pow((a + i*h),2)))

    return sumatoria

print("\nMetodo numerico: Regla Trapezoidal por Jose Santos...\n")
main(1000,0,4)