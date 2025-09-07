def suma_posiciones(nums,target):
    
    for i in range(len(nums)):
        
        for j in range(len(nums)):
            
            if(i!=j):
                
                if nums[i] + nums[j] == target:
                    return [i,j]
                    
            
datos1 = [[2,7,11,15],9]
datos2 = [[3,2,4],6]
datos3 = [[3,3],6]

        
resultado1 = suma_posiciones(datos1[0],datos1[1])
resultado2 = suma_posiciones(datos2[0],datos2[1])
resultado3 = suma_posiciones(datos3[0],datos3[1])


print(resultado1)       
print(resultado2)        
print(resultado3)        
 