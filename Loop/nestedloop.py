#1
for i in range(2, 4):
    for j in range(1, 11):
      if i==j:
        break
      print(i, "*", j, "=", i*j)
    print()

#2
for i in range(2, 4):
    for j in range(1, 11):
      if i==j:
        continue
      print(i, "*", j, "=", i*j)
    print()    