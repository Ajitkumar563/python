 # Write a function named celsius_to_fahrenheit that converts Celsius to Fahrenheit and prints the result.
 # (Formula: (Celsius * 9/5) + 32 = Fahrenheit)
 
def celsius_to_farenheit(Celsius):
    
    fahrenheit = (Celsius * 9/5) + 32 
    print(fahrenheit)
 
 
a=celsius_to_farenheit(45)
print(a) 


# Create a function named simple_calculator that takes three
# parameters: two numbers and an operation (addition or subtraction represented by '+' or '-'),
# and prints the result of the operation

def simple_calculator(num1, num2, operation):
    if operation == '+' :
        result = num1 + num2
     
    
    elif  operation == '-':
        result = num1 -num2
        
    else:
        print("invalid")
        
    print("Result :", result)
    
            
# function call
simple_calculator(3,9,'+')
simple_calculator(9,4, '-')

# Write a function named check_number that takes a number 
# and prints whether it is positive, negative, or zero.
        
def check_number(num):
    if num>0:
        print("positive")
        
    elif num<0:
        print("negative")
        
    else:
        print("zero")            
        
check_number(-3)    


# Write a function named is_odd_even that determines if a number is odd or even 
# without using the modulo operator (%). Hint: Use division or subtraction.    

def is_odd_even(num):
    if num == (num//2)*2 :
        print("even")
        
    else:
        print("odd")    
        
is_odd_even(5)   
is_odd_even(4)     
    