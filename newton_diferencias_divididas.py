# Metódo numerico: Newton con diferencias divididas
# Developed by ~ Fret ~

x = 3.5

xi = [4.4,
	 3.7,
	 3.1]

yi = [-0.68,
     -1.59,
     -1.82]

print("\n\nEncontrando g(x) para: ",x)

print("\n\txi")
for i in xi:
	print("\t",i)

print("\n\tyi")
for i in yi:
	print("\t",i)

# Primera diferencia D'f(xi)
d1_1 = (yi[1]-yi[0])/(xi[1]-xi[0])
d1_2 = (yi[2]-yi[1])/(xi[2]-xi[1])
print("\nPrimera diferencia [D'1]: ",d1_1)
print("Primera diferencia [D'2]: ",d1_2)
print("Para este metodo se considera: ",d1_1)


# Segunda diferencia D''f(xi)
d2_1 = (d1_2-d1_1)/(xi[2]-xi[0]) 
print("\nSegunda diferencia [D''1]: ",d2_1)
print("Para este metodo se considera: ",d2_1)

res = yi[0] + (d1_1*(x-xi[0])) + (d2_1*(x-xi[0])*(x-xi[1]))

print("\nResultado: g(x) = ",res)
