# -*- coding: utf-8 -*-

'''
「パトカー」＋「タクシー」の文字を
先頭から交互に連結して
文字列「パタトクカシーー」を得よ．
'''

str1 = u'パトカー'
str2 = u'タクシー'
str3 = u''

for i,j in zip(str1, str2):
  str3 += i+j

print str3
