

inpt = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'  # NOQA

ret = {}

index_list = [0, 4, 5, 6, 7, 8, 14, 15, 18]
for index, word in enumerate(inpt.split()):
    char = word[0] if index in index_list \
            else word[:2]

    ret[char] = 1 if index in index_list else 2

print(ret)
