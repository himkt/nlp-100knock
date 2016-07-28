require 'numo/narray'
require './knock90_87.rb'


def analogy(mat, v1, v2, v3)
  result = Hash.new
  v4 = v1 - v2 + v3

  mat.shape[0].times do |i|
    v_ = mat[i, true]
    similarity = sim(v4, v_)
    result[i] = similarity
  end

  result.sort{|(_, val1), (_, val2)| val2 <=> val1}[1..10]
end


if __FILE__ == $0
  token2id, id2token, mat = Marshal.load(open('../../data/knock90.dump', 'rb'))
  word_matrix = Numo::Float64.zeros(mat.size, mat[0].size)
  mat.each_with_index do |vector, i|
    vector.each_with_index do |x, j|
      word_matrix[i, j] = x
    end
  end

  vec1 = word_matrix[token2id['Spain'], true]
  vec2 = word_matrix[token2id['Madrid'], true]
  vec3 = word_matrix[token2id['Athens'], true]

  analogy(word_matrix, vec1, vec2, vec3).map{|id, sim| [id2token[id], sim]}.each do |token, sim|
    puts "#{token}\t#{sim}"
  end
end
