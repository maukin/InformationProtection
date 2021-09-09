import caesar1
import re



with open('texts/war.txt', 'rt', encoding="utf-8") as fout:
    poem = fout.read()
    # print(poem)
    poem = (re.sub('[a-z|A-Z]', '', poem)) #.strip()
    print(poem + "\n\n----------------------------------------------------------------------------------------------------------------------------\n")

key_word = "ключ"
NewAlp2 = caesar1.new_alph(key_word)
print(caesar1.caesar2(NewAlp2, poem))

fout1 = open('texts/new_text.txt', 'wt')
fout1.write(caesar1.caesar2(NewAlp2, poem))

fout.close()
fout1.close()
