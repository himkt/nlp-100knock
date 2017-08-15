from knock05 import build_ngram


def union():
    pass


def product():
    pass


def difference():
    pass


inpt1 = 'paraparaparadise'
inpt2 = 'paragraph'

inpt1_char_bigram = build_ngram(inpt1, 2)
inpt2_char_bigram = build_ngram(inpt2, 2)

inpt1_bigram_set = set(inpt1_char_bigram)
inpt2_bigram_set = set(inpt2_char_bigram)

print(inpt1_bigram_set, inpt2_bigram_set)

# 和集合
print(inpt1_bigram_set | inpt2_bigram_set)

# 積集合
print(inpt1_bigram_set & inpt2_bigram_set)

# 差集合
print(inpt1_bigram_set - inpt2_bigram_set)
