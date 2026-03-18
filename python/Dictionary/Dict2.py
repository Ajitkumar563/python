# details ={
#     "Ajit": [32,45,67,76,55],
#     "ram": [33,44,67,70,55],
#     "OM": [32,45,60,79,5],
#     "Ram": [38,45,67,78,50],
#     "Ajeet": [30,40,67,78,57],
# }

# for name, marks in details.items():
#     print(f"Name = {name} | Marks ={sum(marks)}")

# for name, marks in details.items():
#     total =0
#     for mark in marks:
#         total = total + mark
#     print(f"Name = {name} ,Total ={total}")    


# print(details["Ram"][-1])
# print(details["ram"][1])

# """  
# Enter student name = Ajit
# Enter marks =
# Enter marks =
# Enter marks =
# Enter student name = ram
# Enter marks =
# Enter marks =
# Enter marks =
# {
#     "Ajit" : [32, 45, 33],
#     "ram"  : [58, 74, 14],
# }

# """
# details ={}
# for _ in range (0,2):
#     name = input("Enter student name = ")
#     marks = []
#     for _ in range(0, 3):
#         m = int(input("Enter marks = "))
#         marks.append(m)
        
#     details[name] = marks
# print(details)  


# details = {
#     "Ajit" : {"math" : 23, "english" : 54, "hindi" : 98},
#     "Ram" : {"math" : 20, "english" : 50, "hindi" : 88},
#     "ram" : {"math" : 25, "english" : 55, "hindi" : 90},
#     "om" : {"math" : 23, "english" : 54, "hindi" : 98},
# }  

# # How to access
# # print(details["om"]["hindi"])
# # print(details["Ram"]["english"])

# for name, marks in details.items():
#     # print(f"name = {name} | Marks = {marks}")


# details = {
#     "Ajit" : {"math" : 23, "english" : 54, "hindi" : 98, "sst" : 43},
#     "Ram" : {"math" : 20, "english" : 50, "hindi" : 88},
#     "ram" : {"math" : 25, "english" : 55, "hindi" : 90},
#     "om" : {"math" : 23, "english" : 54},
# } 

# for name, marks in details.items():
#     print(name)
#     for k, v in marks.items():
#         print(f"{k} = {v}")
        
# output

# Ajit
# math = 23
# english = 54
# hindi = 98
# sst = 43
# Ram
# math = 20
# english = 50
# hindi = 88
# ram
# math = 25
# english = 55
# hindi = 90
# om
# math = 23
# english = 54        
    
"""
Ajit has scored 323 marks
Ram has scored 412 marks
"""
details = {
    "Ajit" : {"math" : 23, "english" : 54, "hindi" : 98, "sst" : 43},
    "Ram" : {"math" : 20, "english" : 50, "hindi" : 88},
    "ram" : {"math" : 25, "english" : 55, "hindi" : 90},
    "om" : {"math" : 23, "english" : 54},
}  
for name, marks in details.items():
    print(f"name = {name} | Marks = {sum{marks}}")
     
