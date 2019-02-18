# Metódo numerico: Punto fijo o Sustituciones Sucesivas
# Developed by ~ Fret ~

## En este metodo la iteracion se detiene hasta que se 
## Alcancen los 5 decimales en el margen de error

## Despejar la funcion  en terminos de x posibles, evaluar 
## el mas conveniente.

import math

xi = 0
tmp = 0;
e = 0;
i=1;

while True:
	
	xi = ((math.exp(tmp))-2)/2
	#xi = math.exp(tmp*-1)
	e = abs(xi-tmp)
	e_formatted = '{:.20f}'.format(e)

	print(i," xi = ",f'{xi:.20f}',"\t e = ",e_formatted)
	tmp = xi

	if (str(e_formatted).startswith("0.000000")):
		print("\n\nSe llegó a los 6 ceros en el decimal")
		print("\te=",e_formatted," cuando i=",i)
		break;
	i=i+1