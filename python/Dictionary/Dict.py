# Ask number of subjects from the user. Ask the subject name and marks 
# from the user and store that into the dictionary and print it.


# n = int(input("Enter the no of subjects : = "))

# student = {}

# for i in range(n):
#     subject = input("Enter the subjects :")
#     marks = int(input("Enter the marks :"))
    
#     student[subject] = marks
# print(student)    
    
# Enter the no of subjects : = 3
# Enter the subjects :history
# Enter the marks :23
# Enter the subjects :sst
# Enter the marks :111
# Enter the subjects :English
# Enter the marks :67
# {'history': 23, 'sst': 111, 'English': 67}    



# Q2. Given a list of integers, create a dictionary that stores each unique integer as a key and its frequency as the value. Find the integer with the maximum frequency.
# Example Input: [4, 5, 6, 5, 4, 4, 7]
# Expected Output: 4 (Frequency: 3)


# n = [4, 5, 6, 5, 4, 4, 7]
# freq = {}

# for i in n:
#     if i in freq:
#         freq[i] += 1
        
#     else:
#         freq[i] = 1
# max_freq = max(freq, key=freq.get)

# print("freq_dict :",freq)
# print("maximum frequency integer : ",max_freq)
# print("frequency",freq[max_freq])        
        
           
    
# Q3. Create two list. One would be subject name and other would be marks. 
# Join both the list to make it as a dictionary. (The length of two lists should be the same).

# Subjects = ["history", "math", "Science", "English"]
# marks = [45,63,16,77]
# result = dict(zip(Subjects,marks))

# print(result)

# Q4. Write a function that takes a dictionary and a key,
# and returns True if the key is found in the dictionary, otherwise False.

# def check_key(d, key):
#     return key in d

# data = {"apple" : 10, "banana" : 20, "mango" : 30 }

# print(check_key(data, "banana"))
# print(check_key(data, "grapes"))





# Q5. Given two dictionaries, write a function to merge them into a new dictionary. If there is any overlap of keys, the value from the second dictionary should overwrite the one from the first dictionary.
# Dictionary 1:
# {'apple': 3, 'banana': 5, 'cherry': 7}
# Dictionary 2:
# {'banana': 8, 'orange': 10, 'apple': 9}
# Expected Output:
# {'apple': 9, 'banana': 8, 'cherry': 7, 'orange': 10}

# Do dictionaries merge karo, second dictionary overwrite kare

def merge_dict(d1,d2):
    return {**d1 ,**d2}

dict1 = {'apple': 3, 'banana' : 5,'cherry' : 7}
dict2 = 

# Q6. Write a function that updates the values of a dictionary by multiplying them by a given factor only if the value is an integer.
# Initial Dictionary:Factor: 2 (Ask input from user)Output Dictionary:
