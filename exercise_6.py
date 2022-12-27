"""6.I want to build a programm that puts words in alphabetical order
and takes the words from user input rather them an pre build array"""

def alphabetical_order(input_words):
    """Print the given list of words in alphabetical order.

    Parameters:
        input_words (list): A list of words to be sorted and printed.

    Returns:
        None
    """
    sorted_words = sorted(input_words)

    for word in sorted_words:
        print(word)

words = input("Enter a list of words, separated by spaces: ").split()

alphabetical_order(words)
