# -*- coding: utf-8 -*-

"""
42. 係り元と係り先の文節の表示

係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ
"""

from knock41 import parse
from core import Morph, Chunk


if __name__ == '__main__':
    document = parse()

    for sentence in document:
        for chunk in sentence:
            if chunk.dst is not None:

                print("%s\t%s" % (chunk.get_text(), sentence[chunk.dst].get_text()))
