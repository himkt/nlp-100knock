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
        n_morph = len(sentence)
        for i in range(n_morph-2):
            left, center, right = sentence[i:i+3]
            if left['pos'] == right['pos'] == '名詞':
                if center['surface'] != 'の':
                    continue

                l_surface = left['surface']
                c_surface = center['surface']
                r_surface = right['surface']

                print(f'{l_surface}{c_surface}{r_surface}')
