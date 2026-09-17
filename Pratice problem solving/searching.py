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