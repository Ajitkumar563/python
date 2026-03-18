details = {
    "Ajit" : {"math" : 23, "english" : 54, "hindi" : 98, "sst" : 43},
    "Ram" : {"math" : 20, "english" : 50, "hindi" : 88},
    "ram" : {"math" : 25, "english" : 55, "hindi" : 90},
    "om" : {"math" : 23, "english" : 54},
}


print(details.items())
# x =dict(sorted(details.items(),key=lambda x: x[1]["english"]))

x = dict(sorted(details.items(), key=lambda x: sum(x[1].values())))