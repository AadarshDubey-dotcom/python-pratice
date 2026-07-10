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