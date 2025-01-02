homework_text = '''tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''
#remove all spaces and make the text in the one line
spaceless_text = ' '.join(homework_text.split('\n\n'))
#print(spaceless_text)

# make the text in lower case to remove all upper case text in not appropriate places
lower_case_spaceless_text = spaceless_text.lower()
#print(lower_case_spaceless_text)

# remove double spaces after dots
while '.  ' in lower_case_spaceless_text:
    lower_case_spaceless_text = lower_case_spaceless_text.replace('.  ', '. ', 1)
#print(lower_case_spaceless_text)

# splitting the text into separate sentences
sep_sentences = lower_case_spaceless_text.split('. ')

# capitalize the first character for each sentence
capitalized_sentences = [sentence.capitalize() for sentence in sep_sentences]

# join the text again
capitalized_text = '. '.join(capitalized_sentences)
#print(capitalized_text)

# remove incorrect iz and replace it in is
changed_is_text = capitalized_text.replace(' iz ', ' is ')
print(changed_is_text)

# splitting the text info separate sentences
words_in_sent = changed_is_text.split('. ')
# list for the last words
last_words_sentence = []
for sentence in words_in_sent:
    # Remove dot and spaces in the end of the sentence
    sentence = sentence.strip('.').strip()
    # splitting the sentence into words
    words = sentence.split()
    # if the words in the sentence add the last word into variable
    if words:
        last_words_sentence.append(words[-1])

# Sentence creation from the last words
new_sentence = ' '.join(last_words_sentence)

# Adding a new sentence in the end
words_in_sent.append(new_sentence)

# Joining sentences into the text
final_text = '. '.join(words_in_sent)

# showing the result in the console
print(final_text)

# start amount of whitespaces
whitespaces = 0
for i in final_text:  # i - element in final_text
    if i.isspace():
        whitespaces = whitespaces + 1  # if whitespace is found - add +1
print(whitespaces)

