# -*- coding: utf-8 -*-

from knock70 import init
from knock71 import get_stopwords, contain_stop
from sklearn.feature_extraction.text import CountVectorizer
from numpy import array, shape
from sklearn.cross_validation import train_test_split


'''
72. 素性抽出

極性分析に有用そうな素性を各自で設計し，
学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．
'''


def vectorize(features):
    stopwords = get_stopwords()
    X = list()
    y = list()
    cv = CountVectorizer(min_df=10**2)

    for feature in features:
        y.append(1 if feature[0:2] == '+1' else 0)
        X.append(" ".join(list(filter(lambda x: not contain_stop(stopwords, x), feature[3:].split()))))

    cv.fit(X)
    train_X_raw, test_X_raw, train_y, test_y = train_test_split(X, y, test_size=0.2)

    train_X = cv.transform(train_X_raw)
    test_X = cv.transform(test_X_raw)

    return (train_X.toarray(), array([train_y]).T, test_X.toarray(), array([test_y]).T)


if __name__ == '__main__':
    features = init()
    train_X, train_y, test_X, test_y = vectorize(features)
    print(train_X, train_y)
    print(shape(train_X))
