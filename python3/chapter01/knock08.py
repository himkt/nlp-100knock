

# ASCII CODE: http://ee.hawaii.edu/~tep/EE160/Book/chap4/subsection2.1.1.1.html

# ord: char -> int
# chr: int -> char
def cipher(inpt):
    ret = ''
    for char in inpt:
        code = ord(char)
        if 97 <= code <= 122:
            code = 219 - code

        ret += chr(code)
    return ret


def decode(inpt):
    left = 219 - 122
    right = 219 - 97

    ret = ''
    for char in inpt:
        code = ord(char)
        if left <= code <= right:
            code = 219 - code

        ret += chr(code)
    return ret


raw_seq = 'inpt'
print(f'raw: {raw_seq}')

encode_seq = cipher(raw_seq)
print(f'encode: {encode_seq}')
decode_seq = decode(encode_seq)
print(f'decode: {decode_seq}')
