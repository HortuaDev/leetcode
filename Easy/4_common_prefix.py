
def common_prefix(palabras):
    
    prefix = palabras[0]

    for word in palabras[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if(prefix==""):
                return ""    
    return prefix       
        
        
    
       
common_prefix(["flower","flow","flight"])    
