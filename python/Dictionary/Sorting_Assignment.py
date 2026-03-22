 # Q1: Sort dictionary by value (ascending & descending)
 
# d = {1: 2, 4: 3, 2: 1, 0: 0}

# #Ascending 
# asc = dict(sorted(d.items(), key=lambda x :x[1]))
# print(asc)

# desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
# print(desc)

 
# Q2. Write a Python program to count number of items in a dictionary value that is a list.

# d = {
#     "m1": [67, 79, 90, 73, 36],
#     "m2": [89, 67, 84],
#     "m3": [82, 57]
# }  

# count = 0
# for value in d.values():
#     count += len(value)
    
# print("Number of items in dictionary",count)    

    
# Q3. Write a Python program to print a dictionary line by line.    

# d = {
#     "Sam": {"m1": 89, "m2": 56, "m3": 89},
#     "Suresh": {"m1": 49, "m2": 96, "m3": 89}
# }

# for k, v in d.items():
#     print(k)
#     for subject, v in v.items():
#         print(v)
        
# Q4 Write a Python program to convert two lists into a dictionary.

# keys = ["One", "Two", "Three", "Four", "Five"]
# values = [1, 2, 3, 4, 5]        

# d = dict(zip(keys, values))
# print(d)        

# Q5  Create a Python function to sort a dictionary by its values and return that new dictionary.

def sort_dict_by_values(d):
    return dict(sorted(d.items(), keys=lambda x:x[1]))

d = {"a": 3, "b": 1, "c": 2}
print(sort_dict_by_values)
 