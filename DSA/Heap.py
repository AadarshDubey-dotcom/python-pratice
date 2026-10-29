#findKthLargest
import heapq
def findklargest(nums, k):
     heap = []
     for num in nums:
          heapq.heappush(heap, num)
          if len(heap) > k:
               heapq.heappop(heap)
     return heap[0]    
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findklargest(nums, k))

#Calculate height of a heap
import math

def heap_height(n):
     if n < 0:
          return -1
     return math.floor(math.log2(n))

print(heap_height(1))
print(heap_height(7))
print(heap_height(16))

# Minimum Cost of Ropes
import heapq

def min_cost_of_cost(lengths):
     heapq.heapify(lengths)
     total_cost = 0

     while len(lengths) > 1:
          first = heapq.heappop(lengths)
          second = heapq.heappop(lengths)
          
          cost = first + second
          total_cost += cost 
          
          heapq.heappush(lengths, cost)
          
     return total_cost