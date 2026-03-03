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
        