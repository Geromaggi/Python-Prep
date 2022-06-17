from multiprocessing.sharedctypes import Value


class funciones: 
    def __init__(self, lista_numeros):
        if (type(lista_numeros) != list):
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de núemeros enteros')  
        else:
            self.lista = lista_numeros

        
    def es_primo_(self):
        lista_final = []
        for i in self.lista:
            if (self.es_primo(i)):
                lista_final.append(True)
            else:
                lista_final.appned(False)
        return lista_final

    def otras_conversiones (self,origen,destino):
        parametros = ['Celsius','Farenheit','Kelvin']
        lista_conversion = []
        if (str(origen) not in parametros):
            print('Porfavor ingrese nuevamente su origen.')
            return lista_conversion
        if (str(destino) not in parametros):
            print('Porfavor ingrese nuevamente su destino')
            return lista_conversion
        for i in self.lista:
            lista_conversion.append(self.conversion(i,origen,destino))
        return lista_conversion
    
    
    def conversiones (self,origen,destino):
        for i in self.lista:
            print(i,'grados',origen,'son',self.conversion(i,origen,destino),'grados',destino) 

    def factorial__ (self):
        for i in self.lista:
            print('el factorial de',i,'es',self.factorial(i))
    #ESTOS 4 METODOS LOS DEJAMOS ASI. ARRIBA CREAREMOS ESTAS MISMAS FUCNIONES PARA LISTAS. 
    def es_primo(self,x):
        resul = True
        for i in range (2,x):
            if (x % i == 0):
                resul = False
                break
        return resul

    def repetidos (self,lista_numeros):
        repeticiones = 0
        for elem in lista_numeros:
            if (lista_numeros.count(elem)>=2):
                repeticiones = lista_numeros.count(elem)
        return(elem,repeticiones)

    def conversion (self,valor,origen,destino):
        if (origen == 'Celsius'):
            if (destino == 'Celsius'):
                valor_de_destino = valor
            elif (destino == 'Farenheit'):
                valor_de_destino = (valor * 9)/5 + 32
            elif (destino == 'Kelvin'):
                valor_de_destino = valor + 273.15
            else:
                print("parametro de destino incorrecto!")
        elif (origen == 'Farenheit'):
            if (destino == 'Farenheit'):
                valor_de_destino = valor
            elif (destino == 'Celsius'):
                valor_de_destino = ((valor - 32) * 5) / 9
            elif (destino == 'Kelvin'):
                valor_de_destino = valor - 273.15
            else:
                print("parametro de destino incorrecto!")
        elif (origen == 'Kelvin'):
            if (destino == 'Kelvin'):
                valor_de_destino = valor
            elif (destino == 'Celsius'):
                valor_de_destino = valor - 273.15
            elif (destino == 'Farenheit'):
                valor_de_destino = ((valor - 273.15) * 9 / 5) + 32
            else :
                print("parametro de destino incorrecto!")
        else:
            print("parametro de orgen incorrecto!")
        return valor_de_destino   

    def factorial (self,x):
        if (x < 0):
            print("Parametro negativo!")
        elif (type(x) != int ):
            print("Parametro no entero!")
        elif (x > 1):
            x = x * self.factorial(x-1)
        return x

  