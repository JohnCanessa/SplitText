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
