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

Subjects = ["history", "math", "Science", "English"]
marks = [45,63,16,77]
result = dict(zip(Subjects,marks))

print(result)