# -*- coding: utf-8 -*-

from knock70 import init
from knock72 import vectorize
from knock73 import train, h
from numpy import where

'''
74. 予測
73で学習したロジスティック回帰モデルを用い，
与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
その予測確率を計算するプログラムを実装せよ．
'''


def predict(W, X):
    return h(W, X)


def evaluate(y_test, y_predict):
    y_test_t = y_test > 0.5
    y_predict_t = y_predict > 0.5
    res = where((y_test_t == y_predict_t) == True)
    return len(res[0]) / len(y_test)

if __name__ == '__main__':
    features = init()
    X_train, y_train, X_test, y_test = vectorize(features)
    W = train(X_train, y_train)

    predict_y = predict(W, X_test)
    print(evaluate(y_test, predict_y))
