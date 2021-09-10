import caesar1
import re
from collections import Counter
import string




def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])


def removeDuplicateAlphabet(str, alphabet): #удаление ключа из алфавита
    for i in alphabet:
        for j in str:
            if i == j:
                alphabet = alphabet.replace(i, '')
    return alphabet


Alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key_word = "ключ"
index2 = 4
NewAlphabet = removeDuplicateAlphabet(key_word, Alphabet)
NewAlphabet = NewAlphabet[-index2:] + key_word + NewAlphabet[:-index2]


def caesar(NewAlphabet, Alphabet, text):
    Message = []
    for character in text:
        index = Alphabet.index(character)
        character = NewAlphabet[index]
        Message.append(character)
    return ''.join(Message)

spec_chars = string.punctuation + '\n\xa0«»\t—… '


print(NewAlphabet)

with open('texts/war.txt', 'rt', encoding="utf-8") as fout:
    poem = fout.read()
    # print(poem)
    poem = (re.sub('[a-z|A-Z]', '', poem)).lower() #.strip()

    poem2 = remove_chars_from_text(poem, spec_chars)
    poem2 = remove_chars_from_text(poem, string.digits)


    print(poem + "\n\n----------------------------------------------------------------------------------------------------------------------------\n")
    c = Counter(poem)
    new_str = str(c)
    print(new_str)
    # print("\n" + str(c))




# NewAlp2 = caesar1.new_alph(key_word)
# print(caesar1.caesar2(NewAlp2, poem))

print(caesar(NewAlphabet, Alphabet, poem))

fout1 = open('texts/new_text.txt', 'wt')
fout1.write(caesar(NewAlphabet, Alphabet, poem))

fout.close()
fout1.close()
