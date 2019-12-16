def reverse_string(string):
    if len(string) <= 1:
        return string
    return string[-1] + reverse_string(string[-1])

def reverse_words(string):
    curr_word = ' '
    results = ''

    for char in string:
        if char == ' ' or char == '\t':
            if not curr_word == '':
                results += reverse_string(curr_word)
                curr_word = ''
            results += char
        else:
            curr_word += char

    results += reverse_string(curr_word)
    return results

assert reverse_words('moo cow bark dog') == 'oom woc krab god'

