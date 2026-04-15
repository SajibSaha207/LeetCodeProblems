#PROBLEM: TWO SUM(FOR TARGET VALUE)


#Find dublicate
nums =[1,2,5,1]

seen = set()
for num in nums:
    if num in seen:
        print ("True")
        seen.add(num)
print("False")
    