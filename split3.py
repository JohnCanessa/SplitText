import nltk                         # Import the Natural Language Toolkit
from nltk import word_tokenize      # Import the word tokenizer
nltk.download('punkt')              # Download the Punkt tokenizer


# **** define get_words function ****
def get_words(text):

    # **** split text into words ****
    words = word_tokenize(text)

    # **** return list of words ****
    return words


# **** input text ****
text = 'Define which data represents "ham" class and which data represents "spam" class for the machine learning algorithm.'

# **** split includes words: '"ham"', '"spam"', and 'algorithm.' ****
print('text:', text.split())

# **** define list of delimiters ****
delimiters = [' ', '.', '"']

# **** print delimiters ****
print('delimiters: ', delimiters)

# **** define variable words to keep list of processed words ****
words = []

# **** define variable word to keep current word ****
word = ''

# **** loop through each character in text ****
for c in text:
    
    # **** if character is in delimiters list ****
    if c in delimiters:

        # **** add current word in lowercase to list of words (if not blank) ****
        if word != '':
            words.append(word.lower())

            # **** print last word in words list ****
            print('word:', words[-1])

        # **** reset current word ****
        word = ''

    # **** if character is not in delimiters list ****
    else:

        # **** add character to current word ****
        word += c

# **** print list of words ****
print('words:', words)


# **** clear list of words ****
words.clear()

# **** verify list of words has been cleared ****
print('words:', words)

# **** tokenize text ****
words = get_words(text)

# **** display list of tokenized words ****
print('words:', words)
