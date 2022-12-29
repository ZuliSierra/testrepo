#Programa de ejemplo de menú

# from math import pi

# condicion = input("Desea continuar con el cálculo? S/N: ").lower()
# while condicion == "s":

#     radio = float(input("Entre el radio del circulo: "))

#     print("Entra una opción: ")
#     print("a) Calcular diámetro: ")
#     print("b) Calcular el perímetro: ")
#     print("c) Calcular el área: ")
#     opcion = input().lower()

#     if opcion == "a":
#         diametro = 2 * radio
#         print("El diámetro es: {0:.2f}".format(diametro))
#     elif opcion == "b":
#         perimetro = 2 * pi * radio
#         print("El perímetro es: {0:.2f}".format(perimetro))
#     elif opcion == "c":
#         area= pi * radio ** 2
#         print("El área es: {0:.2f}".format(area))
#     else:
#         print("Opción no válida", opcion)

#     condicion = input("Desea continuar con el cálculo? S/N: ").lower()
# print("Bye")


#Programa que determina la posición de un número

# import random
# lista = []
# for i in range(0, 100):
#     lista.append(random.randint(0,100))

# print (lista)

# numero = int(input("Entra el número a buscar: "))

# for i in range(0, 100):
#     if lista[i] == numero:
#         print("El número está en la posición: ", i)
#         break       #Es una salida forzada

#Elaborar un programa que pida un número (input) y dé como salida su tabla de multiplicar.
#Elaborarlo también en forma de función

condicion = input("Desea realizar el cálculo? S/N: ").lower()
while condicion == "s":

    numero = int(input("Entre el numero: "))
    for i in range(0, 11):
        print("El resultado es: ", numero*i)
    
    condicion=input("Desea realizar el cálculo de nuevo? S/N: ").lower()
print("Bye")
