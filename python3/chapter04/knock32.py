from knock30 import parse_neko


if __name__ == '__main__':
    document = parse_neko('../../data/neko.txt.mecab')
    for sentence in document:
        for morph in sentence:
            if morph['pos'] != '動詞':
                continue

            print(morph['base'])
