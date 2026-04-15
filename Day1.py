#PROBLEM: TWO SUM(FOR TARGET VALUE)
numbers = [2,7,11,15]
target = 9
for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    if numbers [i] + numbers [j] == target:
                           print(i,j)
            
                
                    

#Find dublicate
nums =[1,2,5,1]

seen = set()
for num in nums:
    if num in seen:
        print ("True")
        seen.add(num)
print("False")
    