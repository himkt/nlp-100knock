

def parse_neko(fpath):
    document = []
    sentence = []

    for line in open(fpath):
        surface, *feature_ = line.rstrip('\n').split('\t')

        if not feature_ and surface == 'EOS':
            if sentence:
                document.append(sentence)
                sentence = []

            continue

        feature = feature_[0]
        pos, pos1, *_, base, _, _ = feature.split(',')
        morph = {'surface': surface, 'base': base, 'pos': pos, 'pos1': pos1}
        sentence.append(morph)

    return document


if __name__ == '__main__':
    document = parse_neko('../../data/neko.txt.mecab')
