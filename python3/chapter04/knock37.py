from knock30 import parse_neko
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

    freq_list = sorted(word2freq.items(),
                       key=lambda x: x[1],
                       reverse=True)[:10]

    labels, y = list(zip(*freq_list))

    n_label = len(labels)
    X = [i for i in range(n_label)]

    pyplot.bar(X, y, align='center')
    pyplot.xticks(X, labels)
    pyplot.show()
