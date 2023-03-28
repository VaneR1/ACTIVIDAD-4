repetir='S'
while repetir=='S' or repetir=='s':
 print('Ingrese la temperatura en grados celsius: ')
 Celsius=float(input('Temperatura: '))
 print('Presione 1 si desea Grados Fahrenhait')
 print('Presione 2 si desea Grados Kelvin')
 print('Presione 3 si desea Grados Rankine')
 num=int(input('Ingrese el numero: '))
 
 if num==1:
        fahrenhait=round(((9/5)*Celsius)+32,1)

        print(Celsius,'Grados Celsius','es equivalente',fahrenhait,'Grados fahrenhait')

 elif num==2:   
         kelvin=round(Celsius+273.15,1)

         print(Celsius,'Grados Celsius','es equivalente',kelvin,'Grados kelvin')

 elif num==3:
         rankine=round(((Celsius*1.8)+491.67),1) 

         print(Celsius,'Grados Celsius','es equivalente',rankine,'Grados rankine')

 else:
         print('Numero invalido.Ingrese un numero valido')


 repetir=input('¿Desea continuar S/N?')
