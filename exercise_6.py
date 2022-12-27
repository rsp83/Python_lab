"""6.I want to build a programm that puts words in alphabetical order
and takes the words from user input rather them an pre build array"""

def alphabetical_order(words):

    sorted_words = sorted(words)

    for word in sorted_words:
        print(word)

words = input("Enter a list of words, separated by spaces: ").split()

alphabetical_order(words)
