""" Alumno: Daniel Silva
	Ci: 27424058 

	Algoritmo del metodo de bisección"""

from math import *

def f(x):	

	"""Se crea la funcion correspondiente, tomando como parametro la variable a evaluar"""

	return 4-x**2-x**3

def biseccion (a,b,er,num):

	"""parametros del algoritmo biseccion:
		a:limite inferior
		b:limite superior
		er:error relativo
		num:numero de iteraciones"""

	ea = 100													
	i = 0														
	ia = a 														
	ib = b 														
	fm = 0
	if(f(a)*f(b)>0):
		print('no se cumple el valor intermedio')
	else:
		while(i<num) and (ea>er):
			fm = (ia+ib)/2
			if (f(ia)*f(fm)<0):
				ib = fm
		
			if (f(fm)*f(b)<0):
				ia = fm

			i = i+1

			if (i>1):
				ea = ((ib - ia)/ib)*100

	print('la raiz aproximada de la función es: ',fm,' con un error de:' ,ea,'en la iteración ',i)
	

"""ejercicio de la guía con un número máximo de iteraciones puesto de manera arbitraria"""

biseccion(1,2,1,20) 