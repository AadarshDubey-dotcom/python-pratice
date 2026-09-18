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