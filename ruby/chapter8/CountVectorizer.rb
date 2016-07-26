require 'numo/narray'
require 'stopwords'
require 'stemmify'

class CountVectorizer
  attr_accessor :feature_names, :doc_matrix, :token2index

  # tokenizer: lambda function :: string -> Array<string>
  # lowcase: whether if words are lowercases :: bool
  # stop_words: list of stop words :: Array<string>
  # max_features: limitation of feature size :: Float \in [0, 1]
  # TODO: by max_features, zero vectors are sometimes created.
  def initialize(tokenizer, lowercase=true, max_features=0.8)
    @tokenizer = tokenizer
    @lowercase = lowercase

    stop_words = Stopwords::STOP_WORDS
    stop_words.map! {|token| token.stem}
    stop_words.map! {|token| token.downcase} if @lowercase
    @stopwords = stop_words
    @max_feature = max_features
  end

  # features: Each documents' feature :: Array<String> -> NArray::Int64
  def fit_transform(features)
    all_vocaburaries = []
    word_frequency = Hash.new{|hash, key| hash[key] = 0}

    features.each do |feature|
      @tokenizer.call(feature).each do |token|
        token.downcase! if @lowercase
        all_vocaburaries << token
        word_frequency[token] += 1
      end
    end

    all_vocaburaries.uniq!
    word_frequency =  word_frequency.sort{|(_, value1), (_, value2)| value2 <=> value1}
    feature_names = (0...(word_frequency.size * @max_feature).to_i).map{|i| word_frequency[i][0]}

    token2index = {}
    feature_names.each_with_index do |token, i|
      token2index[token] = i
    end

    doc_matrix = Numo::Int32.zeros([features.size, feature_names.size])
    features.each_with_index do |feature, doc_id|
      tokens = []
      @tokenizer.call(feature).each do |token|
        token.downcase! if @lowercase
        tokens << token unless @stopwords.include?(token)
      end

      # BoW representation
      counter = Hash.new{|hash, key| hash[key] = 0}
      tokens.each do |token|
        counter[token] += 1
      end

      counter.each do |token, freq|
        doc_matrix[doc_id, token2index[token]] = freq if token2index[token]
      end
    end

    @doc_matrix = doc_matrix
    @feature_names = feature_names
    @token2index = token2index
    return @doc_matrix
  end
end



if __FILE__ == $0
  cv = CountVectorizer.new(lambda{|s| s.split.map{|token| token.stem}}, 1, 0.8)
  features = ['I am train man which automata and philosophy', 'numerical analysis young man', 'logic programmer']
  p cv.fit_transform(features)
  p cv.feature_names
  p cv.token2index
end
