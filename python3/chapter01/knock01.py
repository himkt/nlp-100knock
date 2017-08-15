
inpt = 'パタトクカシーー'

ret = ''
i = 0
while i < len(inpt):
    ret += inpt[i]
    i += 2
print(ret)

# index_list = (0, 2, 4, 6)
# ret = ''.join(c for i, c in enumerate(inpt)
#               if i in index_list))
# print(ret)
