#Programa que permitirá desplegar listas de DIDs por rangos
#Revisar configuraciòn de entorno python en : https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites

import os #Llamada a módulo 'os' que permite ejecutar comandos del sistema operativo
os.system('clear')

print("Programa para desplegar lista de DIDs")


output=" "
output_lista=" "
rango2=0

while True:
    opcion=input("\n ¿Qué deseas ingresas? \n [1]Digito [2]Rango [3]Imprimir [4]Borrar [Q]Salir\n")

    if opcion == '1':
        DID_digitos=int(input("Digitos: "))   

        output=str(output)+str(DID_digitos)
        print(output)

        #output_lista=str(output_lista)+str(DID_number)
        
            
    if opcion == '2':
        rango1 =int(input("Rango1: "))
        rango2 =int(input("Rango2: \n"))

        '''for i in range(rango1, rango2 + 1):
            DID_rango=str(output_lista)+str(i)
            print(DID_rango)'''

        output="\n" + str(output)+ "[" + str(rango1) + "-" + str(rango2) + "]" 
        print(output)

    if opcion == '3':

        for i in range(0,len(output)):
            print(output[i])

        mul=int(opcion[1])*3

        
    if opcion == '4':
        output=" "
        output_lista=" "
        os.system('clear')

    if opcion == 'q' or opcion =='Q': 
        print("Salida")
        break
