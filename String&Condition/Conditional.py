light = input("enter the light :")

if(light == "Red"):
    print("stop")
elif(light == "Yellow"):
    print("Look")
elif(light == "Green"):
    print("Go")
else:
    print("light is broken") 

# hacker rank promblem        
n = int(input()) 
if n % 2 != 0:  
    print("Weird")
elif 2 <= n <= 5:  
    print("Not Weird")   
    elif 6 <= n <= 20: 
    print("Weird")
else:    
    print("Not Weird")