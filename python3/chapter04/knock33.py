from knock30 import parse_neko


if __name__ == '__main__':
    document = parse_neko('../../data/neko.txt.mecab')
    for sentence in document:
        for morph in sentence:
            if morph['pos'] != '名詞':
                continue

            if morph['pos1'] != 'サ変接続':
                continue

            print(morph['surface'])
