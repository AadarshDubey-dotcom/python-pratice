#1
try:
     n = 0
     res = 100 / n 
     
except ZeroDivisionError:
     print("you can't divide by zero!")

except ValueError:
     print("Enter a vaild number!")
     
else:
     print("Result is", res)
     
finally:
     print("Execution complete.")

#2     
try:
     n = int(input("Enter a number: "))
     res = 100 / n 
     
except ZeroDivisionError:
     print("you can't divide by zero!")

except ValueError:
     print("Enter a vaild number!")
     
else:
     print("Result is", res)
     
finally:
     print("Execution complete.")
