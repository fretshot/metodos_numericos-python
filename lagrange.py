
print("============= Lagrange =============")

x = 7

xi = [7.3,6.5,6.1,5.5]
yi = [-0.28,-1.35,-1.96,-2.74]

print("\nEncontrando g(x) para: ",x)

print("\txi")
for i in xi:
	print("\t",i)
print("\n")
print("\tyi")
for i in yi:
	print("\t",i)


a = (yi[0]*(x-xi[1])*(x-xi[2])*(x-xi[3])) / ( (xi[0]-xi[1])*(xi[0]-xi[2])*(xi[0]-xi[3]))
b = (yi[1]*(x-xi[0])*(x-xi[2])*(x-xi[3])) / ( (xi[1]-xi[0])*(xi[1]-xi[2])*(xi[1]-xi[3]))
c = (yi[2]*(x-xi[0])*(x-xi[1])*(x-xi[3])) / ( (xi[2]-xi[0])*(xi[2]-xi[1])*(xi[2]-xi[3]))
d = (yi[3]*(x-xi[0])*(x-xi[1])*(x-xi[2])) / ( (xi[3]-xi[0])*(xi[3]-xi[1])*(xi[3]-xi[2]))

gx = a+b+c+d

print("\ngx = ",'{:.10f}'.format(gx))