import sys,math

x = 3.25

xi = [2.0,
	 2.5,
	 3.0,
	 3.5]

yi = [3.03,
      3.48,
      4.08,
      4.87]

h1 = abs(xi[0]-xi[1])
h2 = abs(xi[2]-xi[1])
h3 = abs(xi[3]-xi[2])
        
print("\nEncontrando g(x) para: ",x)

print("\txi")
for i in xi:
	print("\t",i)

print("\tyi")
for i in yi:
	print("\t",i)

print("\nIntervalos: ",h1,h2,h3)
if(h1==h2==h3):
    print("\n\t\tLos intervalos son uniformes...")
else:
    print("\n\t\tLos intervalos no son uniformes..")
    print("\nNo aplica este metodo")
    sys.exit()

s = (x-xi[3])/h1
s0 = 1
s1 = s
s2 = (s*(s+1))/math.factorial(2)
s3 = (s*(s+1)*(s+2))/math.factorial(3)
s4 = (s*(s+1)*(s+2)*(s+3))/math.factorial(4)

# Primera diferencia D'f(xi)
d1_1 = (yi[1]-yi[0])
d1_2 = (yi[2]-yi[1])
d1_3 = (yi[3]-yi[2])
print("\nPrimera diferencia [D'1]: ",d1_1)
print("Primera diferencia [D'2]: ",d1_2)
print("Primera diferencia [D'3]: ",d1_3)
print("Para este metodo se considera: {",d1_3,"}")

# Segunda diferencia D''f(xi)
d2_1 = (d1_2-d1_1)
d2_2 = (d1_3-d1_2)
print("\nSegunda diferencia [D''1]: ",d2_1)
print("Segunda diferencia [D''2]: ",d2_2)
print("Para este metodo se considera: {",d2_2,"}")

# Tercera diferencia D'''f(xi)
d3_1 = (d2_2-d2_1)
print("\nTercera diferencia [D'''1]: ",d3_1)
print("Para este metodo se considera: {",d3_1,"}")

gx = yi[3]*s0 + (d1_3*s1) + (d2_2*s2) + (d3_1*s3)

print("\n\tg(x) = ",gx)