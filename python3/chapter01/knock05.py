

def build_ngram(inpt, n):
    n_len = len(inpt)
    return [inpt[i:i+n] for i in range(n_len-n+1)]


if __name__ == '__main__':
    inpt = 'I am an NLPer'
    inpt_words = inpt.split()

    print(build_ngram(inpt_words, 2))
    print(build_ngram(inpt, 2))
