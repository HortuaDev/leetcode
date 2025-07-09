def parentesis_valido(texto):
    
    caracteres = {')': '(', '}': '{', ']': '['}
    
    stack = []
    
    for caracter in texto:
        
        if caracter in caracteres.values():
            stack.append(caracter)
            
        elif caracter not in caracteres.values():
            
            if len(stack) == 0:
                return False
            
            if stack[-1] != caracteres[caracter]:
                return False
            
            stack.pop()        
         
    return len(stack) == 0     
    
print(parentesis_valido("({}[])"))