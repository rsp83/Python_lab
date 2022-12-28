""" 8.Find the longest word in a sentence:
 Write a Python program that asks the user to enter a sentence
 and then prints the longest word in that sentence"""

#user input
sentence = input("Enter a sentence: ")

#Split the sentence into a list of words with the method split()
words = sentence.split()

#initialize a variable to store the longest word
longest_word = ""
#Iterate through each word in the list of words
for word in words:
    #If the current word is longer than the longest word we've seem so far,
    # update the longest word to be the current word
    if len (word) > len(longest_word):
        longest_word = word

#print the longest word
print("The longest word is:", longest_word)
