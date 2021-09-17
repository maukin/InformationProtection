import caesar1 as c
import re
from collections import Counter
import string


def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])


def input_key():
    print("Введите ключ:")
    func_key = input().lower()
    while (not (c.is_unique(func_key))) or (len(func_key) > 32 or len(func_key) < 0) or c.isContainsRussianLetters(func_key):
        print("Неправильный ключ, повторите ввод")
        func_key = input().lower()
    return func_key


def is_digit(ind):
    try:
        int(ind)
        return True
    except ValueError:
        return False


def input_index():
    print("Введите индекс сдвига:")
    func_index = input()
    while not is_digit(func_index) or (int(func_index) > 32 or int(func_index) < 0):
        print("Неправильный индекс, повторите ввод")
        func_index = input()
    return func_index


def input_message():
    print("Введите сообщение:")
    func_message = input().lower()
    return func_message


spec_chars = string.punctuation + '\n\xa0«»\t—… '
spec_chars2 = "!\"#$%&'()*+-./:;<=>?@[\]^_`{|}~" + "\xa0,\xa0"

Alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
FrequencyOfLetters = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'

while 1:
    print("\n1 - Шифр цезаря с ключом и сдвигом\n2 - Шифр цезаря модифицированный\n3 - Шифрование и дешифрование главвы книги\n0 - Завершение программы\nВведите номер:")
    number = input()
    if number.isdigit():
        number = int(number)
        if number == 1:
            print("~~~~\tШифр цезаря с ключом и сдвигом\t~~~~")
            key = input_key()
            index = input_index()
            message = input_message()

            # print("Зашифрованный текст: " + c.caesar(key, index, message))
            c.caesar(key, index, message)

        elif number == 2:
            print("~~~~\tШифр цезаря модифицированный\t~~~~")
            key2 = input_key()
            message2 = input_message()

            # print("Зашифрованный текст: " + c.caesar2(key2, message2))
            c.caesar2(key2, message2)

        elif number == 3:
            print("~~~~\tШифрование и дешифрование главы книги\t~~~~")
            with open('texts/WarAndPeaceOriginal.txt', 'rt') as text_original:
            # with open('texts/war.txt', 'rt', encoding="utf-8") as text_original:

                # ccc1 = text_original.read()
                # ccc1 = Counter(re.findall(r'(?=([а-я]{2}))', ccc1))
                # print("Original: ")
                # print(ccc1.most_common(10))

                poem = text_original.read()
                poem = (re.sub('[a-z|A-Z|A-Z|a-z]', '', poem)).lower()  # .strip()

                poem2 = remove_chars_from_text(poem, spec_chars)
                poem2 = remove_chars_from_text(poem, string.digits)

                ccc1 = Counter(re.findall(r'(?=([а-я]{2}))', poem2)).most_common(10)
                print("Original: ")
                # print(ccc1)

                new_list2 = str(ccc1)
                new_list2 = remove_chars_from_text(new_list2, string.digits)
                new_list2 = remove_chars_from_text(new_list2, spec_chars2).split()
                print(new_list2)



                # num = Counter(poem2)
                # new_str = str(num)
                # print(new_str)
                # print("\n" + str(num))

            key = 'ключ'
            index = 3
            # key = input_key()
            # index = input_index()

            # c.caesar(key, index, poem2)

            with open('texts/WarAndPeaceEncrypted.txt', 'w') as text_encrypted:
                text_encrypted.write(c.caesar(key, index, poem2))

            new_text = c.caesar(key, index, poem2)

            letters_decr = Counter("".join([ch for ch in new_text if ch in Alphabet]))
            # print(letters_decr)
            # list_of_letters = list(letters_decr.items())
            # list_of_letters.sort(key=lambda i: i[1])
            # list_of_letters.reverse()
            # print(list_of_letters)

            Message3 = []

            new_list = str(letters_decr)
            # new_list = str(list_of_letters)
            new_list = remove_chars_from_text(new_list, spec_chars)
            new_list = remove_chars_from_text(new_list, string.digits)
            new_list = new_list[7:]
            # print(new_list)

            with open('texts/WarAndPeaceDecrypted.txt', 'wt') as text_decrypted:
                for char_new in new_text:
                    try:
                        index_new = new_list.index(char_new)
                        new_char = FrequencyOfLetters[index_new]
                        Message3.append(new_char)
                    except ValueError:
                        Message3.append(char_new)
                text_decrypted.write(''.join(Message3))



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ БИГРАМНЫЙ АНАЛИЗ ТУТ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            with open('texts/WarAndPeaceDecrypted.txt', 'rt') as text_decrypted2:
                ccc = text_decrypted2.read()
                ccc = Counter(re.findall(r'(?=([а-я]{2}))', ccc)).most_common(10)
                print("New: ")
                # print(ccc)

                new_list3 = str(ccc)
                new_list3 = remove_chars_from_text(new_list3, string.digits)
                new_list3 = remove_chars_from_text(new_list3, spec_chars2).split()
                print(new_list3)


            for a in range(len(new_list3)):
                if new_list3[a] != new_list2[a]:
                    print(new_list3[a])





            text_original.close()
            text_encrypted.close()
            text_decrypted.close()

        elif number == 0:
            break