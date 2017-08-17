from knock30 import parse_neko


def get_np(sentence):
    OUTSIDE, BEGIN, INSIDE = 0, 1, 2
    ret = []
    np = []

    state = OUTSIDE
    for morph in sentence:
        if morph['pos'] == '名詞':
            if state == OUTSIDE:
                state = BEGIN

            elif state in [BEGIN, INSIDE]:
                state = INSIDE

            np.append(morph['surface'])

        else:
            if np:
                # if state is INSIDE, there are at least
                # two morph in np (this is phrase)
                if state == INSIDE:
                    ret.append(np)
                np = []

            state = OUTSIDE

    return ret


if __name__ == '__main__':
    document = parse_neko('../../data/neko.txt.mecab')
    for sentence in document:
        for np in get_np(sentence):
            print(''.join(np))
