# Sort list ascending  
num = [12,3,4,55,64,2]

num.sort()
print(num)

# Sort list descending  
num = [12,3,4,55,64,2]

num.sort(reverse=True)
print(num)

# Bubble sort implementation  
def bubble_sort(arr):
     for i in range(len(arr)):
          for j in range(0, len(arr)-i-1):
               if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
     return arr

number = [65,23,55,76,43,77,87]     
sorted_list = bubble_sort(number)

print("Sorted List :", sorted_list)
"""Logic Flow
Input list → ek list jisme numbers hain.

Outer loop → jitni baar list ke elements hain utni baar repeat hoga.

Inner loop → har adjacent pair compare karega.

Swap elements → agar left element bada hai toh dono ko swap karo.

Repeat until sorted → jab tak list ascending order me na aa jaye."""

#Selection sort  
def selection_sort(arr):
     for i in range(len(arr)):
          min_idx = i
          for j in range(i+1, len(arr)):
               if arr[j] < arr[min_idx]:
                    min_idx = j 
          arr[i], arr[min_idx] = arr[min_idx], arr[i]          
     return arr

number = [23,43,21,5,6,77]     
result = selection_sort(number)

print("sorted list :", result)
"""Logic Flow (Selection Sort)
Input list → ek list jisme numbers hain.

Outer loop → har position ke liye ek pass chalega.

Find minimum → unsorted part me sabse chhota element dhoondo.

Swap with current → us minimum ko current position ke saath swap karo.

Repeat until sorted → jab tak poori list sorted na ho jaaye."""

# Insertion Sort 
def insertion_sort(arr):
     for i in range(1, len(arr)):
          key = arr[i]
          j = i-1
          while j >= 0 and arr[j] > key:
               arr[j+1] = arr[j]
               j-=1
               
          arr[j+1] = key
     return arr
     
number = [23,43,2,3,44,5]     
result = insertion_sort(number)

print("Result :", result)
"""📌 Logic Flow (Insertion Sort)
Input list → ek list jisme numbers hain.

Outer loop → second element se start karke har element ko apni sahi jagah pe insert karna hai.

Key element → current element ko key variable me store karo.

Shift elements → agar left side ke elements key se bade hain toh unhe ek step right shift karo.

Insert key → jab sahi position mil jaaye toh key ko insert karo."""

# Merge Sort
def merge_sort(arr):
     if len(arr) > 1:
          mid = len(arr) // 2
          left_half = arr[:mid]
          right_half = arr[mid:]
          
          merge_sort(left_half)
          merge_sort(right_half)
          
          
          i = j = k = 0
          
          while i < len(left_half) and j < len(right_half):
               if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
               else:
                    arr[k] = right_half[j]
                    j += 1
               k += 1
               
          while i < len(left_half):
               arr[k] = left_half[i]
               i += 1
               k += 1
               
          while j < len(right_half):   
               arr[k] = right_half[j]
               j += 1
               k += 1
               
     return arr     
     
number = [12,34,5,6,3,33]     
result = merge_sort(number)

print("Result :", result)
"""📌 Logic Flow (Merge Sort)
Divide list → list ko recursively do halves me todte raho jab tak single element na bache.

Conquer → har half ko individually sort karna (recursion se).

Merge → sorted halves ko merge karke final sorted list banani."""

## Quick Sort
def quick_sort(arr):
     if len(arr) <= 1:
          return arr
     else:
          pivot = arr[len(arr) // 2]
          left = [x for x in arr if x < pivot]
          mid = [x for x in arr if x == pivot]
          right = [x for x in arr if x > pivot]
          return quick_sort(left) + mid + quick_sort(right)
          
number = [23,45,6,5,55,28]          
result = quick_sort(number)

print("result :", result)
"""Logic Flow (Quick Sort)
Choose pivot → ek element ko pivot select karo (usually first, last, or middle).

Partition list → pivot se chhote elements left side, bade elements right side.

Recursive sort → left aur right sublists ko recursively sort karo.

Combine → sorted left + pivot + sorted right = final sorted list."""

#Sort strings by length  
#Ek program likho jo ek list of strings ko unke length ke basis par ascending order me sort kare.