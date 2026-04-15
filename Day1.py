

#THIRD MAXMUM NUMBER
nums = [3,2,1]
nums = set(nums)

if len(nums)< 3:
    print(max(nums))
else:
    nums= sorted(nums, reverse=True)
print(nums[2])  

  