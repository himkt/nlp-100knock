# -*- coding: utf-8 -*-

str = "stressed"

puts str.reverse

arr = str.split(//)
i = arr.size-1

loop do
  print arr[i]
  i -= 1
  break if i == -1
end
