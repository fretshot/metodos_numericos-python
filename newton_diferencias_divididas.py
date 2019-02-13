# Metódo numerico: Newton con diferencias divididas
# Developed by ~ Fret ~

x = 3.25

xi = [2.2,
	 2.5,
	 3,
	 3.5]

yi = [3.03,
      3.48,
      4.08,
      4.87]

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
d1_3 = (yi[3]-yi[2])/(xi[3]-xi[2])
print("\nPrimera diferencia [D'1]: ",d1_1)
print("Primera diferencia [D'2]: ",d1_2)
print("Primera diferencia [D'3]: ",d1_3)
print("Para este metodo se considera: {",d1_1,"}")


# Segunda diferencia D''f(xi)
d2_1 = (d1_2-d1_1)/(xi[2]-xi[0]) 
d2_2 = (d1_3-d1_2)/(xi[3]-xi[1]) 
print("\nSegunda diferencia [D''1]: ",d2_1)
print("Segunda diferencia [D''2]: ",d2_2)
print("Para este metodo se considera: {",d2_1,"}")

# Tercera diferencia D'''f(xi)
d3_1 = (d2_2-d2_1)/(xi[3]-xi[0])
print("\nTercera diferencia [D'''1]: ",d3_1)
print("Para este metodo se considera: {",d3_1,"}")

res = yi[0] + (d1_1*(x-xi[0])) + (d2_1*(x-xi[0])*(x-xi[1])) + (d3_1*(x-xi[0])*(x-xi[1])*(x-xi[2]))
print("\ng(x) = [",yi[0],"]\n + [(",d1_1,")(",x,"-",xi[0],")]\n + [(",d2_1,")(",x,"-",xi[0],")(",x,"-",xi[1],")]\n + [(",d3_1,")(",x,"-",xi[0],")(",x,"-",xi[1],")(",x,"-",xi[2],")]")
print("\nResultado: g(x) = ",res)
