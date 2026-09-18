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