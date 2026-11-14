def twosum(number, traget):
     left = 0
     right = len(number) - 1
     
     while left < right:
          current_sum = number[left] + number[right]
          
          if current_sum == traget:
               return [
                    left + 1,
                    right + 1,
               ]
          elif current_sum < traget:
               left += 1
          else:     
               right -= 1
     return []          
               
print(twosum([2,7,11,15], 9))               