from knock30 import parse_neko
from collections import Counter
from matplotlib import pyplot
from matplotlib import rc

pyplot.style.use('ggplot')
font = {'family': 'YuGothic'}  # NOTE: use YuGothic for Japanese
rc('font', **font)


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

    freq_list = word2freq.values()
    X, y = list(zip(*Counter(freq_list).items()))
    pyplot.scatter(X, y)
    pyplot.show()
