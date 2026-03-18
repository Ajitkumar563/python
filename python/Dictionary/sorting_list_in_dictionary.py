details = {
    "Ajit" : [23, 45, 76, 87, 77],
    "Ram" : [20, 47, 76, 89, 87],
    "ram" : [30, 48, 96, 97, 77],
    "om" : [20, 40, 77, 85,27],
}

# print(details.items())
x = dict(sorted(details.items(), key =lambda x: sum(x[1])))

# x = dict(sorted(details.items(), key=lambda x: x[1][-1]))
# x = dict(sorted(details.items(), key = lambda x: max(x[1])))

print(x)
for name, marks in x.items():
    print(f"Name = {name}, marks = {sum(marks)}")