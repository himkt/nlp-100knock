# -*- coding: utf-8 -*-

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

list = {}

str.split(" ").each do |word|
  list[word] = word.size
end

