# -*- coding: utf-8 -*-

str1 = "paraparaparadise"
str2 = "paragraph"

arr1 = str1.split(//)
arr2 = str2.split(//)
=begin
diff is not interactive, but undirectional.
it has a basic, and takes a difference from basic.
=end


p (arr1 + arr2).uniq # union
p arr1 - arr2
# p ((arr2 - arr1) + (arr1 - arr2)) # diff
p arr2.product(arr1) # product

union = []
diff = []
prod = []

arr1.each do |item|
  union << item if !union.include?(item)
end

arr2.each do |item|
  union << item if !union.include?(item)
end

arr1.each do |item|
  diff << item if !arr2.include?(item)
end

=begin
arr2.each do |item|
  diff << item if !arr1.include?(item)
end
=end

arr1.each do |item1|
  arr2.each do |item2|
    prod << [item1, item2]
  end
end

p union
p diff
p prod
