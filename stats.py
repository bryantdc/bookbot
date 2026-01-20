word_count = 0


def get_num_char(text):
    char_dict={}
    lower_text = text.lower()
    for char in lower_text:
        if char not in char_dict:
            char_dict.update({char: 1})
        elif char in char_dict:
            char_dict[char] += 1
    return char_dict

def get_num_words(text):
    word_count = len(text.split())
    return word_count