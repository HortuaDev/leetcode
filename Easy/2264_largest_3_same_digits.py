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
            
        for i in range(len(opciones[1:])):
            
            
            if opciones[i+1] > opciones[i]:
                maximo = opciones[i+1]    
            
    return maximo    
    
print("Resultado: ",evaluador("6777133339"))
print("Resultado: ",evaluador("2300019"))
print("Resultado: ",evaluador("42352338"))