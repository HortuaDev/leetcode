def numero_afortunado(numeros):
    
    frecuencia = {}
    max_numero = 0
    
    for numero in numeros:
        contador = 0
        
        for numero_interno in numeros:
            
            if numero == numero_interno:
                contador+=1 
    
        if contador == numero: 
            frecuencia[numero] = contador 
            
            if frecuencia[numero] > max_numero:
                max_numero = frecuencia[frecuencia[numero]]                         
    
    if max_numero == 0:
        return -1
    else:
        return max_numero    
            
print(numero_afortunado([2,2,3,4]))    
    
    