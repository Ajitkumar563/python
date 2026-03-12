# n  = int(input("enter the no ="))

# number = []

# # Loop
# for i in range(n):
#     num = int(input("Enter the number ="))
#     number.append(num)
    
# print(number)    

# Remove duplicate numbers

# numbers = [1, 6, 5, 1, 1, 1, 10, 1, 6]
# unique = []

# for i in numbers:
#     if i not in unique:
#         unique.append(i)
        
# print(unique)        


#  Ask 10 numbers from the user and put them into the list. Now remove
#   all the even numbers from that list.

number = []

# Ask 10 number 
for i in range(10):
    n = int(input("Enter the number = "))
    number.append(n)
    
# Remove the number 
for num in number:
    if num %2 == 0:
        number.remove(num)    
        
print(number)        

    
