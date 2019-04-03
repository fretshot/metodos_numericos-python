x = 0
y = 0
z = 0

i = 1
print("--------------------------    GAUSS -SEIDEL    ---------------------------")
print("0"," xi =  0.0000000000","\tyi =  00.0000000000","\tzi =  00.0000000000")
print("--------------------------------------------------------------------------")

while True:
	
	xi = (4+(1*y)+(1*z))/2
	yi = (3-(1*z)-(1*x))/-2
	zi = (-5+(1*x)+(1*y))/2
	
	"""
	xi = (8+y+z)/8
	yi = (4+(2*xi)-z)/4
	zi = (5-xi+(3*yi))/5
	"""
	ex = '{:.10f}'.format(abs(xi - x))
	ey = '{:.10f}'.format(abs(yi - y))
	ez = '{:.10f}'.format(abs(zi - z))
	
	print(i," xi = ",f'{xi:.10f}',"\tyi = ",f'{yi:.10f}',"\tzi = ",f'{zi:.10f}')
	print("\tex = ",ex,"\tey = ",ey,"\tez = ",ez)
	print("--------------------------------------------------------------------------")

	x = xi;
	y = yi;
	z = zi;

	if (str(ex).startswith("0.000")):
		print("\nSe llegó a los 2 ceros [e=0.001] en el decimal")
		break;

	i+=1
	