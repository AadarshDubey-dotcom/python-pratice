#Linear Search Program  
def linear_search(arr, traget):
     for i in range(len(arr)):
          if arr[i] == traget:
               return i
     return -1

number = [10,20,30,40,50]
search_element = 30

result = linear_search(number, search_element)

if result != -1:
     print(f"Element {search_element} found at index {result}")
else:
     print(f"Element {search_element} not found")

"""Logic Flow
Input list → ek list jisme elements stored hain.

Target element → jis element ko search karna hai.

Loop through list → har element ko check karo.

Condition check → agar element target ke equal hai → found.

Return result → index ya message print karo."""

#Binary Search Program
def Binary_search(arr, target):
     low = 0 
     high = len(arr) - 1
     
     while low <= high:
          mid = (low + high) // 2
          
          if arr[mid] == target:
               return mid
          elif arr[mid] < target:
               low = mid + 1
          else:
               high = mid - 1
               
     return -1        
     
number = [10,20,30,40,50,60]     
search_number = 40

result = Binary_search(number, search_number)

if result != -1:
     print(f"Element {search_number} found at index {result}")
else:
     print(f"Element {search_number} not found")

"""Logic Flow
Sorted list → Binary search sirf sorted list pe kaam karta hai.

Initialize pointers → low = 0, high = len(list)-1.

Find mid → mid = (low + high) // 2.

Compare element →

Agar arr[mid] == target → element found.

Agar arr[mid] < target → right half search karo (low = mid+1).

Agar arr[mid] > target → left half search karo (high = mid-1).

Repeat until found → loop chalta rahega jab tak element mil jaye ya low > high ho jaye."""

#Search in String  
text = input("enter the string :")
word = input("enter the word :")

if word in text:
     print(word,"word found in text")
else:
     print("not found.")
"""Logic Flow
Input string → user se ek string lo.

Input word → jis word ko search karna hai wo lo.

Check condition → if word in string: use karo.

Return result → print karo ki word exist karta hai ya nahi."""     
     