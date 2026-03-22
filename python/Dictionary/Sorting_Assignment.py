 # Q1: Sort dictionary by value (ascending & descending)
 
# d = {1: 2, 4: 3, 2: 1, 0: 0}

# #Ascending 
# asc = dict(sorted(d.items(), key=lambda x :x[1]))
# print(asc)

# desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
# print(desc)
 
# Q2. Write a Python program to count number of items in a dictionary value that is a list.

d = {
    "m1": [67, 79, 90, 73, 36],
    "m2": [89, 67, 84],
    "m3": [82, 57]
}  
 