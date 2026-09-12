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
#Even numbers filter  
lis = [1,2,3,4,5,6]
new = []

for n in lis:
     if n % 2 == 0:
          new.append(n)

print(new)          

#Second largest element
lis = [34,21,65,32,34]
unique_list = list(set(lis))
unique_list.sort()
second_large = unique_list[-2]

print(second_large)

#Word frequency count
word =  "hello world hello python world"
n = word.split()
dic = {}
for w in n:
     if w in dic:
          dic[w] += 1
     else:
          dic[w] = 1
     
print(dic)
"""Logic Flow
Input text → ek string lo (sentence/paragraph).

Split words → split() function se words ki list banao.

Loop through words → har word ko check karo.

Dictionary store → dictionary me word ko key aur count ko value rakho.

Update count → agar word pehle se hai to +1 karo, nahi hai to 1 se start karo.

Print result → final dictionary print karo."""