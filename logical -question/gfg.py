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

#Convert all 0s to 5"
"""Replace Method: Python ka built-in .replace('0', '5') method use karke saare '0' ko '5' mein badal dete hain."""
n = [2,0,4,0,6,0]
n = [5 if x == 0 else x for x in n]
print(n)

def convertZeroToFive(n):
     str_num = str(n)
     new_str = str_num.replace("0", "5")
     
     return int(new_str)
     
number = 670202100
result = convertZeroToFive(number)
print(result)