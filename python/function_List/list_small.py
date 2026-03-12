nums =[12,34,98,-98,77]

largest =nums[0]


for i in range(0, len(nums)):
    if nums[i]> largest:
        largest=nums[i]
print("Largest :" , largest)        
    