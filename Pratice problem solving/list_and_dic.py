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