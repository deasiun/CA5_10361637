#Author Des McCann
# DBSid 10361637
# CA5 Part 2 test calcultor
#note that reduce and lambda are usedfor about 50% of hte functions, 
#list comprehension is used for the other 50%


###########################################

import math

class cal(object):

#addition (1)
    def add(self, x):
    
        number_types = (int, long, float, complex, list)
 
        if isinstance(x, number_types):
         return reduce(lambda a,b:a+b,x)
        else:
            raise ValueError
#subtraction (2)
    def subtract(self, x):
#        return reduce(lambda a,b:a-b,x)
        number_types = (int, long, float, complex, list)
     
        if isinstance(x, number_types):
         return reduce(lambda a,b:a-b,x)
        else:
            raise ValueError

#multiplication (3)
    def multiply(self, x):
        number_types = (int, long, float, complex, list)
        if isinstance(x, number_types):
         return reduce(lambda a,b:a*b,x)
        else:
            raise ValueError

#integer division (4)           
    def intdivide(self, x):
        
        number_types = (int,list)
        if isinstance(x, number_types):
         return reduce(lambda a,b:a/b,x)
        else:
            raise ValueError
    
# integer division remainder (5)          
    def remainder(self, x):
        number_types = (int,list)
        if isinstance(x, number_types):
         return reduce(lambda a,b:a%b,x)
        else:
            raise ValueError

# floating point division.(6)
    def fdivision(self, x):
        number_types = ( float, complex,list)
        if isinstance(x, number_types):
         return reduce(lambda a,b:a/b,x)
        else:
            raise ValueError
            
 
# sign change (7)
    def signchange(self,x):
        number_types = (int, long, float, complex, list)
 
        if isinstance(x, number_types):

            signchanger = [-anitem for anitem in x]
            return signchanger 
        else:
            raise ValueError

   
# absolute value (8)
    def absolute(self,x):
        number_types = (int, long, float, complex,list)
 
        if isinstance(x, number_types):
            absoluter = [abs(anitem) for anitem in x]
            return absoluter
        else:
            raise ValueError

# square of each value (9)
    def square(self,x):
        number_types = (int, long, float, complex,list)
 
        if isinstance(x, number_types):
            squarer = [anitem*anitem for anitem in x]
            return squarer
        else:
            raise ValueError

# Squareroot (10)
    def squareroot(self,x):
        number_types = (int, long, float,list)
 
        if isinstance(x, number_types):
            sqrter = [math.sqrt(anitem) for anitem in x]
            return sqrter 
            
           
        else:
            raise ValueError
# factorial (11) 
    def factorial(self,x):
        number_types = (int, long,list)
 
        if isinstance(x, number_types):
            facto = [math.factorial(anitem) for anitem in x]      
            return facto    
        else:
            raise ValueError
            
        
print" Program ran!" 
