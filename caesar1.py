from collections import defaultdict

Alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def is_unique(s):
    return len(s) == len(set(s))

# print ("Шифр Цезаря - первый вариант")
# print("Введите сообщение:")
# Message = input().lower()
#
#
# print("Введите ключ:")
# key = input().lower()
# while (not (is_unique(key))) and (len(key) > 32 or len(key) < 0):
#     print("Неправильный ключ, повторите ввод")
#     key = input().lower()
#
#
# print("Введите индекс:")
# index = int(input())
# while index > 32 or index < 0:
#     print("Неправильный индекс, повторите ввод")
#     index = int(input())


# def removeDuplicate(str): #удаление дубликатов в строке
#     if (len(str)) < 2:
#         return str
#     result = []
#     for i in str:
#         if i not in result:
#             result.append(i)
#     return ''.join(result)


# def removeDuplicateAlphabet(str, alphabet): #удаление ключа из алфавита
#     for i in alphabet:
#         for j in str:
#             if i == j:
#                 alphabet = alphabet.replace(i, '')
#     return alphabet
#
#
# def caesar(NewAlphabet, Alphabet, text):
#     Message = []
#     for character in text:
#         index = Alphabet.index(character)
#         character = NewAlphabet[index]
#         Message.append(character)
#     return ''.join(Message)


# NewAlphabet = removeDuplicateAlphabet(key, Alphabet)
# NewAlphabet = NewAlphabet[-index:] + key + NewAlphabet[:-index]

# print('\nold:' + Alphabet)
# print('new:' + NewAlphabet)
# print("Зашифрованный текст: " + caesar(NewAlphabet, Alphabet, Message))





# print ("\n\nШифр Цезаря - второй вариант")
#
# print("Введите ключ:")
# key2 = input().lower()
# while (not (is_unique(key))) and (len(key2) > 32 or len(key2) < 0):
#     print("Неправильный ключ, повторите ввод")
#     key2 = input().lower()
#
#
# print("Введите сообщение:")
# Message2 = input().lower()


alphabet = 'а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,ъ,ы,ь,э,ю,я'
alphabet = alphabet.split(',')

def new_alph(key_word):
    key_word = list(key_word)
    # print('Old Alphabet:', '\t', alphabet)
    new_alphabet = []
    counter = 0
    for i in range(len(alphabet)):
        new_alphabet.append(key_word[counter])
        counter += 1
        if counter == len(key_word):
            counter = 0
    # print('New Alphabet:\t', len(new_alphabet), '\t', new_alphabet)
    return new_alphabet


# NewAlp = new_alph(key2)
# print('New Alphabet:', '\t', NewAlp)


def caesar2(NewAlphabet, text):
    Message = []
    for character in text:
        if character in alphabet:
            index = alphabet.index(character)
            new_char = NewAlphabet[index]
            new_index = alphabet.index(new_char)
            character2 = alphabet[((index + new_index) % len(alphabet))]
            # print("индекс " + str((index + new_index) % len(alphabet)))
            Message.append(character2)
        else:
            Message.append(character)
    return ''.join(Message)


# print(caesar2(NewAlp, Message2))


