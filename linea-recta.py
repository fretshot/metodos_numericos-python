# -*- coding: utf-8 -*-
import math

banner = '''
        +=======================================+
        |....Metodos Numericos - Linea Recta....|
        +---------------------------------------+
        |#Author: Oscar Alemán                  |
        |#Contact: fretshot@gmail.com           |
        |#Date: 10/04/2019                      |
        +=======================================+
        |............ FIME  --  UANL ...........|
        +---------------------------------------+
'''

print (banner)

x = [2.4,4.8,5.1,10.5]

for potencia in range (1,7):
	sumatoria = 0
	for i in x:
		sumatoria = sumatoria + math.pow(i,potencia)

	print ("Sumatoria potencia ",potencia,": ",sumatoria)