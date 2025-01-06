# functions for task 2
import random
import string

def generate_random_dicts(num_dicts, num_keys, key_length, seed):
    random.seed(seed)
    list_of_dicts = []
    for i in range(num_dicts):
        new_dict = {}
        for i in range(num_keys):
            key = ''.join(random.choices(string.ascii_lowercase, k=key_length))
            value = random.randint(0, 100)
            new_dict[key] = value
        list_of_dicts.append(new_dict)
    return list_of_dicts

def combining_dictionaries(list_of_dicts):
    combined_dict = {}
    for i in range(len(list_of_dicts)):
        current_dict = list_of_dicts[i]
        for k, v in current_dict.items():
            if k not in combined_dict:
                combined_dict[k] = [[i + 1, v]]
            else:
                combined_dict[k].append([i + 1, v])
    return combined_dict

def final_diction(combined_dict):
    final_dict = {}
    for k, v in combined_dict.items():
        if len(v) == 1:
            final_dict[k] = v[0][1]
        else:
            max_value = v[0]
            for i in v:
                if i[1] > max_value[1]:
                    max_value = i
            final_dict[k + '_' + str(max_value[0])] = max_value[1]
    return final_dict


result = generate_random_dicts(num_dicts=3, num_keys=5, key_length=1,seed=42)
combine_result = combining_dictionaries(result)
final_result = final_diction(combine_result)
# print(result)
# print(combine_result)
print(final_result)


# functions for task 3
homework_text = '''tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

def remove_double_newlines(text):
    return ''.join(text.split('\n\n')).lower()

spaceless_text = remove_double_newlines(homework_text)
#print(spaceless_text)

def adding_correct_space(text):
    result = []
    length = len(text)
    for i in range(length):
        result.append(text[i])
        if text[i] == '.' and (i + 1 < length and text[i + 1] != ' '):
            result.append(' ')
    return ''.join(result)

correct_space = adding_correct_space(spaceless_text)
#print(correct_space)

def capitalize_start_letter(text):
    sep_sentences = text.split('. ')
    capitalized_sentences = [sentence.capitalize() for sentence in sep_sentences]
    capitalized_text = '. '.join(capitalized_sentences)
    return capitalized_text

capitalize_letter = capitalize_start_letter(correct_space)
#print(capitalize_letter)

def change_iz_is(text):
    changed_is_text = text.replace(' iz ', ' is ')
    return changed_is_text

changing_iz = change_iz_is(capitalize_letter)
#print(changing_iz)

def words_in_sentences(text):
    words_in_sent = text.split('. ')
    last_words_sentence = []
    for sentence in words_in_sent:
        sentence = sentence.rstrip('.').strip()
        words = sentence.split()
        if words:
            last_words_sentence.append(words[-1])
    new_sentence = ' '.join(last_words_sentence)
    new_paragraph = text + ' ' + new_sentence + '.'
    return new_paragraph

text_with_new_paragraph = words_in_sentences(changing_iz)
print(text_with_new_paragraph)

def count_whitespace(new_text):
    whitespaces = 0
    for i in new_text:
        if i.isspace():
            whitespaces = whitespaces + 1
    return whitespaces

text_whitespace = count_whitespace(text_with_new_paragraph)
print(f" I've got {text_whitespace} whitespaces in the homework")