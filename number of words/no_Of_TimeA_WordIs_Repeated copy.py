"""
You are writing an essay. You don't want the any word to appear very frequently. 
Write a program that will take your essay as input (maybe from a file) and print the number of times each unique word appears in your essay.
"""
# import regular expression
import re
essay=""
file = open('essay.txt','r')
for each in file:
    essay += each
file.close()
# to substitute the special characters by space
essay=re.sub('[^a-zA-Z0-9]+'," ",essay)
# split every words in the essay using split function.
essay=essay.split(" ")
# use set to make list with each word in a list.
UniqueWords=set(essay)
# loop to find the number of times a word is used
for i in UniqueWords:
    print(f"The word '{i}' is present in the essay {essay.count(i)} times") # to find the number of times a word is used i have used count function.



"""
OP:
enter a essay:The natural cycle of our ecosystem is vital for the survival of organisms. We all should take care of all the components that make our nature complete. We should be sure not to pollute the water and air as they are gifts of Nature.
The natural cycle of our ecosystem is vital for the survival of organisms We all should take care of all the components that make our nature complete We should be sure not to pollute the water and air as they are gifts of Nature 
The word 'the' is present in the essay 3 times
The word 'as' is present in the essay 1 times
The word 'vital' is present in the essay 1 times
The word 'should' is present in the essay 2 times
The word 'that' is present in the essay 1 times
The word 'to' is present in the essay 1 times
The word 'sure' is present in the essay 1 times
The word 'all' is present in the essay 2 times
The word 'natural' is present in the essay 1 times
The word 'care' is present in the essay 1 times
The word 'they' is present in the essay 1 times
The word 'is' is present in the essay 1 times
The word 'our' is present in the essay 2 times
The word 'We' is present in the essay 2 times
The word 'components' is present in the essay 1 times
The word 'nature' is present in the essay 1 times
The word 'take' is present in the essay 1 times
The word 'and' is present in the essay 1 times
The word 'pollute' is present in the essay 1 times
The word 'cycle' is present in the essay 1 times
The word 'for' is present in the essay 1 times
The word 'The' is present in the essay 1 times
The word 'are' is present in the essay 1 times
The word 'Nature' is present in the essay 1 times
The word 'complete' is present in the essay 1 times
The word 'not' is present in the essay 1 times
The word 'air' is present in the essay 1 times
The word 'be' is present in the essay 1 times
The word 'water' is present in the essay 1 times
The word 'survival' is present in the essay 1 times
The word 'gifts' is present in the essay 1 times
The word 'of' is present in the essay 4 times
The word 'ecosystem' is present in the essay 1 times
The word 'organisms' is present in the essay 1 times
The word 'make' is present in the essay 1 times
"""