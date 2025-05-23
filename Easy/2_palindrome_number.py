def encuentra_palindromo(num):
    
    num = str(num)
    
    count = len(num)-1
    
    for i in range(len(num)):
        
        if num[i] != num[count]:
            return False
                
        count = count -1
        
    return True    
        
        
        
print(encuentra_palindromo(124421))    