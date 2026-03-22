 # Q1: Sort dictionary by value (ascending & descending)
 
d = {1: 2, 4: 3, 2: 1, 0: 0}

#Ascending 
asc = dict(sorted(d.items(), key=lambda x :x[1]))
print(asc)

desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(desc)
 