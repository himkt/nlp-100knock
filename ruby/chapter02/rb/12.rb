# -*- coding: utf-8 -*-

=begin
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
=end

o1 = open('../../data/col1.txt', 'w')
o2 = open('../../data/col2.txt', 'w')

open('../../data/hightemp.txt', 'r') do |input|
  while line = input.gets
    item = line.split(/\t/)
    o1.print("#{item[0]}\n")
    o2.print("#{item[1]}\n")
  end
end

o1.close
o2.close
