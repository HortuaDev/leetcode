def unir_listas_ordenadas(lista1,lista2):
    
    nueva_lista = []
    
    for num1 in lista1:
        nueva_lista.append(num1)
    
    
    for num2 in lista2:
        nueva_lista.append(num2)
    
    for i in range(len(nueva_lista)):
        for j in range(len(nueva_lista)):
            if i != j:
                
                if nueva_lista[j] > nueva_lista[i]:
                    aux = nueva_lista[i]
                    nueva_lista[i] = nueva_lista[j] 
                    nueva_lista[j] = aux
    print(nueva_lista)          
    
unir_listas_ordenadas([1,2,4],[1,3,8])    