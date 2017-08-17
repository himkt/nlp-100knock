from knock30 import parse_neko
from matplotlib import pyplot
pyplot.style.use('ggplot')


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

    sorted_freq = sorted(word2freq.values(),
                         reverse=True)

    freq_rank = [[rank, freq] for rank, freq in enumerate(sorted_freq,
                                                          start=1)]

    X, y = list(zip(*freq_rank))
    pyplot.scatter(X, y)
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.show()
