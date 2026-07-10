#Simple Triangle
n = 4 
for i in range(1, n+1):
     for j in range(i):
          print("*", end=" ")
     print()

#Pyramid
n = 4 
for i in range(1, n+1):
     print(" "*(n-i) + "* "*i)
     
#Inverted Triangle
n = 4
for i in range(n, 0, -1):
     for j in range(i):
          print("*", end=" ")
     print()   

#Number Triangle
n = 4
for i in range(1, n+1):
     for j in range(1, i+1):
          print(j, end=" ")
     print()                 

#Floyd’s Triangle
n = 4
num = 1
for i in range(1, n+1):
     for j in range(i):
          print(num, end=" ")
          num += 1 
     print()          