def __gcd(a, b): 
    if (a == 0 or b == 0): 
    	return 0
    if (a == b): 
    	return a 
    if (a > b):  
        return __gcd(a - b, b) 
              
    return __gcd(a, b - a)  
def coprime(a, b): 
    if ( __gcd(a, b) == 1): 
        print("1") 
    else: 
        print("0")      
a = 5; b = 6
coprime(a, b)  
  
a = 8; b = 16
coprime(a, b) 
