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

# count vowels in string
word = input("enter the str :")

def count_vowel(word):
     vowel = "aeiouAEIOU"
     count = 0
     for ch in word:
          if ch in vowel:
               count += 1
     return count
print(count_vowel(word))
"""📌 Logic of Vowel Count
Input string lo.

Ek set banao vowels ka: a, e, i, o, u (lowercase + uppercase).

Har character ko loop me check karo.

Agar character vowel hai → count badhao.

Final count return karo."""

# Longest word in sentence  
Sentence = input("enter the Sentence :")

def Longest_sentence(Sentence):
     words = Sentence.split()
     longest = ""
     for w in words:
          if len(w) > len(longest):
               longest = w 
     return longest
          
print(Longest_sentence(Sentence))        

"""📌 Logic of Longest Word
Input sentence lo.

Sentence ko split karke words ki list banao.

Har word ki length check karo.

Jo word sabse bada hoga usko store karo.

Final longest word return karo."""

#remove duplicate
#📌 Method 1: Using set()
lis = ["harsh", "adarsh","harsh", "pandit"]

def remove_duplicate(lis):
     return list(set(lis))

print(remove_duplicate(lis))     

#Method 2: Maintain Order
lis = ["harsh", "adarsh","harsh", "pandit"]

def remove_duplicate(lis):
     result = []
     for item in lis:
          if item not in result:
               result.append(item)
     return result
print(remove_duplicate(lis))     