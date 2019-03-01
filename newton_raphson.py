# Metódo numerico: newton raphson
# Developed by ~ Fret ~

## En este metodo la iteracion se detiene hasta que se 
## Alcancen los 5 decimales en el margen de error

## Derivar la funcion una vez

import math

xi = 0
tmp = 1;
e = 0;
i=1;

while True:
	
	#xi = tmp - ((((2*math.pow(tmp, 2)) - (6*tmp) - 2)) / ((4*tmp) - 6) ) # 2x^2 - 6x - 2
	xi = tmp - (((math.exp(3*tmp))-4)/(3*math.exp(3*tmp))) # e^3x - 4
	e = abs(xi-tmp)
	e_formatted = '{:.10f}'.format(e)

	print(i," xi = ",f'{xi:.10f}',"\t e = ",e_formatted)
	tmp = xi

	if (str(e_formatted).startswith("0.00000")):
		print("\nSe llegó a los 5 ceros [e=0.00000] en el decimal")
		print("\te=",e_formatted," cuando i=",i," \txi=",xi)
		break;
	i=i+1