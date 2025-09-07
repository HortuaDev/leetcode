def encuentra_palindromo(numbers):
    
    numbers = str(numbers)
    contador = len(numbers)-1
    validador = False
    
    
    for num in numbers:
        
        if num == numbers[contador]:
            validador = True
        else:
            validador = False
            break    
            
        contador -= 1
        
        
    if validador:
        return True
    else:
        return False
        
        
encuentra_palindromo(124421)    