#Reverse a string
word = input("enter the str :")

def reverse_word(word):
     rev = ""
     for ch in word:
          rev = ch + rev
     return rev     
     
print(reverse_word(word))     
