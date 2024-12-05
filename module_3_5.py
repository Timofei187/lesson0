def single_root_words(root_word = 'Строка', *other_words):
    same_words = []
    rw = root_word.lower()
    for string in other_words:
        sl = string.lower()
        if rw.find(sl) >= 0 or sl.find(rw) >= 0:
            same_words.append(string)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)