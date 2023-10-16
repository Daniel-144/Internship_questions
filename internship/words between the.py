"""
Problem #1
Read a passage from a file. (If you don't know how to handle files in Python, you can hardcode a long passage)
Count the number of times the word 'the' followed by another 'the' without 'a' in between.

Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

answer is 4 (The king, the forest, The King the next).
"""
# get the passage as a input form the user.
# split the word
def findA(counter,i,passage):
    for k in range(i,counter+1):
        if passage[k]=="a":
            return 0
        break
    return 1
        

passage=input("enter the passage")
passage=passage.lower()
passage=passage.split(" ")
print(passage)
count=0
for i in range(len(passage) - 1):
     for j in range(len(passage)):
         print (passage[i],passage[j])
         if passage[i]=="the" and passage[j]=="the":
             counter=j-i
             count+=findA(counter,i,j,passage)
print(count)
           
