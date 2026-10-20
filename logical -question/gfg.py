#Jumping through While - Python
"""Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).

Example:

Input: x = 10
Output: 1 4 9
Explanation:From 1 to 10, numbers in powers of 2 are, 12, 22, 32 as 1, 4 and 9."""
def printIncreasingPower(x):
    i = 1
    # Loop to jump in powers of 2
    while(i*i <= x):
        print (i*i , end = " ")
        i += 1
        
print(printIncreasingPower(10))        