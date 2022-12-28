"""10. Write a Python script that reads a text file : to do : done
and counts the number of words in it : to do: done
the script should take the file name as an input and print the word count to the console : to do: done

 When you execute the script: the first argument should be the name of the script,
 and the second argument should be the file name.
 ex :  python3 python word_count.py text_file.txt """



import sys

def count_words(filename):
    # Open the file
    # Uses read mode ('r')
    # Assigns a file object to the variable f
    with open(filename,'r') as f:
        # Read the contents of the file
        contents = f.read()

    words = contents.split()

    #return the length of the list of words
    return len(words)

# Get the file name from the command line arguments
filename = sys.argv[1]

# Call the function and print the result
word_count = count_words(filename)
print(f"The file {filename} has {word_count} words.")
