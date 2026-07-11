#Rotate array
arr = [1,2,3,4]
k = 2
rot = arr[k:] + arr[:k]
print(rot)     

#Check duplicates
arr = [1,2,3,4,5,3]
if len(arr) != len(set(arr)):
     print("duplicate is exist")
else:
     print("duplicate is not exist")

#Prefix Sum
arr = [1,2,3,4]
prefix = []
current_sum = 0

for x in arr:
     current_sum += x
     prefix.append(current_sum)
     
print(prefix)          