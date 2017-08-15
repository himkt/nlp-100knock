
inpt1, inpt2 = 'パトカー', 'タクシー'
ret = ''

for c1, c2 in zip(inpt1, inpt2):
    ret += f'{c1}{c2}'  # f-string is available after python3.6

print(ret)
