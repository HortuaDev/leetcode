def evaluador(numero):
    
    count = 0
    num = 0
    opciones = []
    maximo = ""
    
    for i in range(len(numero[1:])):
        
        primero = numero[i]
        segundo = numero[i+1]
        
        if primero == segundo:
            count+=1
            num = numero[i]
        else:
            count=0
            num = ""
    
        if count == 2:
            
            result = num+num+num
            
            opciones.append(result)
            
            result = 0
    
    if len(opciones) != 0:
        
        maximo = opciones[0]
            
        for i in opciones:
            
            if i > maximo:
                maximo = i    
            
    return maximo    
    
print("Resultado: ",evaluador("4818042931906802860005960222213336669500011846936171709111"))