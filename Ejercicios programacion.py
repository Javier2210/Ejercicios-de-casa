print (f'Ejercicio 1')
 
c = 23
d = 21
suma2 = c + d
resta = c - d
multiplicacion2 = c * d
division = c / d 

print (f'Suma:',suma2)
print (f'Resta:',resta)
print (f'Multiplicacion:',multiplicacion2)
print (f'Division:',division)

print(f'Ejercicio 2')

castellano = 18
ingles = 20
matematicas = 17
resultado = castellano+ingles+matematicas/3
print(f'Castellano 18')
print(f'Ingles 20')
print(f'Matematicas 17')
print(f'El promedio de las siguientes materias es' ,resultado)

print(f'Ejercicio 3')

numero = int(input("Indica un numero: "))
if (numero % 2) == 0: print (f'El número es par') 
else: print (f'El número es impar')

print (f'Ejercicio 4')

numero2 = int(input("Indica un numero del 10 al 20: "))
if numero2 in range(9,21): 
    print(f'El numero esta en el rango seleccionado')
else:
    print(f'El numero no esta en el rango seleccionado')
