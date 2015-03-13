# -*- coding: utf-8 -*-

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

list = {}

str.split(" ").each_with_index do |word, i|
  i += 1
  if ([1,5,6,7,8,9,15,16,19].include?(i))
    list[word] = word[0].upcase
  else
    list[word] = word[0..1]
  end
end
