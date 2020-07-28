"""
Nombre: funciones.py
Objetivo: Muestra la operaciòn de las funciones en python
Autor: Antonio Rodriguez
Fecha: 27/07/2020
"""

def mensaje():
	print ("Hola desde mensaje")



def regresamensaje():
	return "Saludo desde el regresa mensaje"


def printmensaje(msg):
	print (msg)



def suma(n1, n2):
	return n1+n2


def resta(n1, n2):
	return n1-n2


def mult(n1, n2):
	return n1*n2


def div(n1, n2):
	return n1/n2



def main():

	ciclo = 'S'
	while ciclo == 'S' or ciclo =='s':
		#invocamos funcion mensaje
		mensaje()
		#invocamos funcion regresamensaje
		print (regresamensaje())
		#invocamos funcion printmensaje
		printmensaje("Hola te saludo...")
		
		#leemos los datos por teclado
		a = int(input("Ingresa el primer numero entero: "))
		b = int(input("Ingresa el segundo numero entero: "))
		#Invocamos la funcion suma
		print ("La suma es: ", suma(a,b))
		print ("=========================")
		print ("La resta es: ", resta(a,b))
		print ("=========================")
		print ("La multiplicacion es: ", mult(a,b))
		print ("=========================")
		print ("La division es: ", div(a,b))
		print ("=========================")

		
		#preguntamos por otra operacion
		ciclo = input("¿Desea otra operacion (s/n)?")
	else:
		print ("*** Fin de programa")

if __name__ == "__main__":
	main()
