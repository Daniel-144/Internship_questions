"""
4.
Encode the user input using the following alg, using the encode Key (a number)
For each word in the odd position, move each letter in the word by the number of positions mentioned in the key.
For words in the even position, reverse the word and then do the same as the odd position
Eg - Key 2, input sentence "I am the King"
Output K oc vjg ipkM
"""
# input a number to encode the string.
key=int(input("enter any number:"))
inputString=input("enter a string:")
# the input string is splited and stored in a list.
listString=inputString.split(" ")
# initialized a empty string to store the encrypted string
encryptedstring=""
# loop to traverse through the list
for words in listString:
    # the words in even positoin should be reversed(the index starts from zero)so words had reversed the words with odd index.
    if (listString.index(words) % 2 != 0):
        # by using slicing and the step value as -1 the letters of the string are moved backwards.
        words=words[::-1]
    # loop to traverse through the letters in the words
    for letters in words:
        # the letter is converted into the ascii value with the help of ord function.
        letters=ord(letters)
        # the converted Ascii value is added with the key.
        letters+=key
        # then the value is converted into a character.
        letters=chr(letters)
        # the Ascii value which was converted into a character is stored in the list.
        encryptedstring+=letters
    # to strore a space at the end of each word.
    encryptedstring+=" "
print(f'encrypted string:{encryptedstring}')

"""
OP:
enter any number:2
enter a string:I am the King
encrypted string:K oc vjg ipkM 

"""

