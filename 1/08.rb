# -*- coding: utf-8 -*-

def chipher(str)
  chiphed = ''
  str.split(//).each do |char|
    if char.ord >= 97 && char.ord <= 122
      chiphed += (219 - char.ord).chr('UTF-8')
    else
      chiphed += char
    end
  end
  return chiphed
end

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

p chipher(str)
