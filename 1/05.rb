# -*- coding: utf-8 -*-

str = "I am an NLPer"

def word(str)
  arr = str.split(" ")
  bigram(arr)
end

def char(str)
  arr = str.gsub!(' ','').split(//)
  bigram(arr)
end

def bigram(arr)
  i = 0
  arr.size.times do
    puts "#{arr[i]}, #{arr[i+1]}" if arr[i+1] != nil
    i += 1
  end
end

word(str)

char(str)
