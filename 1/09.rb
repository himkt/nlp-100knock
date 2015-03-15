# -*- coding: utf-8 -*-

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
str2 = ""

str.split(" ").each do |word|
  arr = word.split(//)
  if arr.size > 4
    h = arr.shift
    f = arr.pop
    c = arr.shuffle
    c.unshift(h)
    c.push(f)
    str2 += "#{c.join} "
  else
    str2 += "#{arr.join} "
  end
end

puts str2
