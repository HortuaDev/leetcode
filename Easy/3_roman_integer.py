def numero_romano(num):

    
    numbers = {"I":1,
               "V":5,
               "X":10,
               "L":50,
               "C":100,
               "D":500,
               "M":1000}
    
    total = 0
    before = 0
    
    for letter in reversed(num):
        
        actual = numbers[letter]
        
        if actual < before:
            total -= actual
        else:
            total+=actual    
        before = actual        
    
    print(total)
        
    

numero_romano("CDLIV")    