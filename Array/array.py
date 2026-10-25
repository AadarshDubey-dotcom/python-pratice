#1. Traversal (Saare Elements ko Ek-Ek Karke Dekhna)
songs = ["ironman", "spiderman", "koi mil gay", "hello"]

for song in songs:
     print(song)

"""2. Insertion (Naya Element Add Karna)
List mein naya element add karne ke liye alag-alag tareeqe hote hain:

append(): List ke aakhir mein element add karta hai.

insert(index, value): Kisi specific position par element dalta hai."""

"""3. Deletion (Element Hatana)
List se kisi element ko hatane ke liye:

remove(value): Naam ke hisaab se element hatata hai.

pop(index): Index ke hisaab se element hatata hai (agar index na dein toh aakhiri element hata deta hai)."""

#Two SumProblem: Ek list di gayi hai aur ek target number. Aapko aise do numbers ke indices (positions) batane hain jinka sum target ke barabar ho.Logic: Hum ek Dictionary (hash map) ka use karte hain taaki har number ka complement (target - num) check kar sakein ki pehle se dekha hai ya nahi. Isse time complexity $O(n)$ ho jaati hai.

def twoSum(nums, target):
     seen = {}
     
     for i, num in enumerate(nums):
          complement = target - num
          if complement in seen:
               return [seen[complement], i]
          seen[num] = i
          
     return []     
     
print(twoSum([2,7,11,15],9))     