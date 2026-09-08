#Reverse a string
word = input("enter the str :")

def reverse_word(word):
     rev = ""
     for ch in word:
          rev = ch + rev
     return rev     
     
print(reverse_word(word))     
"""Logic of Reverse String
Input string lo (example: "hello").

Ek empty string banao jo reversed result store kare.

Har character ko loop me ulta order me add karo.

Final result return karo."""