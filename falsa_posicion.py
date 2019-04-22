# Metódo numerico: falsa posicion
# Developed by ~ Fret ~

## En este metodo la iteracion se detiene hasta que se 
## Alcance 1 cero en los decimales del margen de error

## Despejar la funcion  en terminos de x posibles, evaluar 
## el mas conveniente.

#xi = ((math.exp(tmp))-2)/2
#xi = math.exp(tmp*-1)
#xi = (math.exp(3*tmp))-4


import math

xi = 0
tmp = 0;
e = 0;
i=1;

a=0
b=1

fb=16
fa=-3


print("i:",i-1," \tb:",b," \tf(b):",fb," \ta:",f'{a:.10f}'," \txi:",f'{xi:.9f}',"\tf(a):",f'{fa:.10f}'," \te: -----------")

while True:
	a=xi

	#fa= 2*(math.pow(a,2))- (6*a) -2 # Para 2x^2 - 6x - 2
	fa = (math.exp(3*a))-4 # Para e^3x - 4
	xi = a - ((fa*(b-a))/(fb-fa))
	
	e = abs(xi-tmp)
	e_formatted = '{:.10f}'.format(e)

	print("i:",i," \tb:",b," \tf(b):",fb," \ta:",f'{a:.10f}'," \txi:",f'{xi:.10f}'," \tf(a):",f'{fa:.10f}'," \te:",e_formatted)

	tmp = xi

	if (str(e_formatted).startswith("0.000")):
		print("\n\nSe llegó a los 3 ceros [e = 0.001] en el decimal")
		print("\te=",e_formatted," cuando i=",i," \txi=",xi)
		break
	i=i+1