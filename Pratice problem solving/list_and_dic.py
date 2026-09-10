#Reverse a list  
#Method 1: Using reverse() (in‑place)
lis = [1,2,3,4]
lis.reverse()
print(lis)

#Method 4: Loop Logic
lis = [1,2,3,4]
rev = []
for n in lis:
     rev = [n] + rev 
print(rev)     

#Find max and min
#built in function max() and min()
lis = [1,2,3,4]

print("Max :", max(lis))
print("Min :", min(lis))

#Method 2: Loop Logic
lis = [1,2,3,4]

max_num = lis[0]
min_num = lis[0]

for n in lis:
     if n > max_num:
          max_num = n 
     if n < min_num:
          min_num = n 
print("Max :", max_num)          
print("Min :", min_num)