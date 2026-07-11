# 🔹 Insertion
arr = [1, 2, 3]
arr.append(4)        # [1, 2, 3, 4]
arr.insert(1, 99)    # [1, 99, 2, 3, 4]

# 🔹 Deletion
arr = [10, 20, 30]
arr.remove(20)       # [10, 30]
arr.pop(1)           # [10]
del arr[0]           # []

# 🔹 Searching
arr = [5, 10, 15]
print(10 in arr)     # True
for x in arr:
    if x == 15:
        print("Found")

# 🔹 Updating
arr = [1, 2, 3]
arr[1] = 99          # [1, 99, 3]


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

