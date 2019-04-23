
import math

print ("\n============ Secante ============")

temp1 = 0
ftemp1 = math.exp(3*temp1)-4
print("1  xi: ",f'{temp1:.8f}',"\tfxi: ",f'{ftemp1:.8f}',"\te: --------")

temp2 = 1
ftemp2 = math.exp(3*temp2)-4
print("2  xi: ",f'{temp2:.8f}',"\tfxi: ",f'{ftemp2:.8f}',"\te: --------")

i = 2
while True:
    xi = temp2-((ftemp2*(temp2-temp1))/(ftemp2-ftemp1))
    fxi = math.exp(3*xi)-4
    e = '{:.8f}'.format(abs(xi-temp2))

    print(i," xi: ",f'{xi:.8f}',"\tfxi: ",f'{fxi:.8f}',"\te: ",e)
    
    temp1 = temp2
    ftemp1 = ftemp2
    temp2 = xi
    ftemp2 = fxi
   

    if (str(e).startswith("0.000")):
        print("\n\nSe llego a los 3 ceros [e=0.000] en el decimal")
        print("\te=",e," cuando i=",i," \txi=",f'{xi:.10f}')
        break

    i=i+1