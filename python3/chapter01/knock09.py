import random


def typoglycemia(inpt):
    ret = []
    for word in inpt.split():
        if len(word) > 4:
            subchar_list = list(word[1:-1])
            random.shuffle(subchar_list)
            substr = ''.join(subchar_list)
            word = f'{word[0]}{substr}{word[-1]}'

        ret.append(word)

    return ' '.join(ret)


inpt = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'  # NOQA
print(inpt)
print(typoglycemia(inpt))
