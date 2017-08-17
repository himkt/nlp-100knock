from knock30 import parse_neko


if __name__ == '__main__':
    document = parse_neko('../../data/neko.txt.mecab')
    word2freq = {}

    for sentence in document:
        for morph in sentence:
            word = morph['base']

            if word in word2freq.keys():
                word2freq[word] += 1

            else:
                word2freq[word] = 1

    for word, freq in sorted(word2freq.items(),
                             key=lambda x: x[1],
                             reverse=True)[:10]:
        print(f'{word}\t{freq}')
