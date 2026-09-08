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

#check palindrome
word = input("enter the str :")

def palindrome_check(word):
     temp = ""
     for ch in word:
          temp = ch + temp     
     if word == temp:
          print("this is palindrome.")
     else:
          print("this is not palindrome")
     
print(palindrome_check(word))     
"""📌 Logic of Palindrome Check
Input lo (string ya number).

Uska reverse banao.

Compare karo:

Agar original == reversed → Palindrome.

Agar alag hai → Not Palindrome."""
