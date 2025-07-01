def add_two_numbers(l1,l2):
    
    # los convierto en listas de str para poder recorrelos
    
    lista_1 = str(l1)
    lista_2 = str(l2)
    
    # almaceno los tamaños para condicionar dos funcionamientos
    # si ambos son de igual tamaño o si uno es mas grande que el otro
    tamanio_1 = len(lista_1)
    tamanio_2 = len(lista_2)
    
    # creo un almacenador de valores mayor a 10 (lo usaremos despues)
    carry = 0
    
    # evaluo si el tamaño de los arreglos son iguales
    
    if tamanio_1 == tamanio_2:
        
        # creo un contador con la posicion mas alta menos 1 para poder 
        # recorrer el arreglo desde el final pero al reves
        # ejemplo 
        # [1,2,3] -> posiciones [0,1,2]
        # al reves, "posicion" valdra [2] = tamaño 3 - 1 = 2;
        # [3,2,1] -> posiciones [2,1,0]
        
        posicion = len(lista_1)-1
        
        # recorro el arreglo al reves
        for _ in reversed(lista_1):
        
            # declaro dos variables con el contenido de su posicion
        
            num_1 = int(lista_1[posicion])
            num_2 = int(lista_2[posicion])
            
            # evaluo si la suma es mayor igual a 10
            
            if num_1 + num_2 >= 10:
                
                # en caso afirmativo (>= 10)
                
                # divido el numero en caracteres
                
                resultado_caracteres = str(num_1 + num_2)
                
                # se asigno el ultimo numero (cero en este caso)
                # al resultado
                
                result = int(resultado_caracteres[1])
                
                # y almaceno el primer caracter como numero 
                carry = int(resultado_caracteres[0])
            
            else:
                # en caso de no ser > = 10
                # sumo todos los valores mas el carry (valor almacenado)
                # al resultado
                # y lo restablesco a cero (el carry)
                result = num_1 + num_2 + carry 
                carry = 0   
            
            print("result: ", result)
            
            # voy restando el iterador posicion -1 para ir de atras hacia delante
            posicion-=1
        
    else:
        
        if tamanio_1 > tamanio_2:
            
            posicion = len(lista_1)-1
            
            aux_lista_2 = list(lista_1)
            lista_2 = list(lista_2)
            
            for i in range(len(lista_2)):
                
                aux_lista_2[i] = lista_2[i]
            
            print(aux_lista_2)   
        else:
            posicion = len(lista_2)-1
            print("el segundo es mas grande")     
    
    
    
        
    
add_two_numbers(99999999,8888)    