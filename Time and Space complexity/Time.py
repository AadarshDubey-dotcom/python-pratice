"""🧩 Step‑by‑Step Learning Path
1. Understand Big‑O Basics
Time Complexity → How runtime grows with input size.

Space Complexity → How memory usage grows with input size.

Common classes:

O(1) → Constant (e.g., accessing list element by index).

O(n) → Linear (e.g., iterating over a list).

O(log n) → Logarithmic (e.g., binary search).

O(n²) → Quadratic (e.g., nested loops)."""

"""2. Practice with Python Loops
Single loop → O(n).

Nested loop → O(n²).

Loop halving input (while n > 1: n//=2) → O(log n).

python
# O(n) example
def linear_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False"""

# O(n²) example
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(log n) example
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

"""3. Analyze Built‑in Operations
Lists: append O(1), pop(0) O(n), sort O(n log n).

Sets/Dicts: add/get O(1) average, O(n) worst case.

Strings: slicing O(k), concatenation O(n)."""

"""4. Work on Recursion
Learn recurrence relations (e.g., T(n) = 2T(n/2) + O(n)).

Example: Merge Sort → O(n log n).

Example: Fibonacci naive recursion → O(2^n)."""

"""5. Space Complexity Examples
Extra arrays → O(n).

Constant variables → O(1).

Recursion stack → O(n) for depth n."""