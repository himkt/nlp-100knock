require './knock72.rb'
require 'numo/narray'
require './CrossValidation.rb'


class LogisticRegressionModel
  def initialize
    @eta = 0.01
    @threshold = 0.7
  end
  
  
  def h(x)
    z = x.dot(@w)
    return 1 / (1 + Numo::NMath.exp(-z))
  end


  def fit(x, y)
    @w = Numo::Float64.new([x.shape[1], 1]).rand * 10
    10.times do |t|
      @w = @w - @eta * x.transpose.dup.dot(y - h(x)) # x.T.dot(h(x) - y): gradient
      puts "#iter: #{t}, accuracy: #{score(x, y)}"
    end
  end


  def predict(x)
    probabilities = h(x)
    return probabilities > @threshold
  end


  def predict_prob(x)
    return h(x)
  end


  def score(x, y)
    predicted_class = predict(x)
    num_data = predicted_class.shape[0]

    py = predicted_class.to_a
    ry = y.to_a

    num_correct = 0
    num_data.times do |t|
      num_correct += 1 if py[t] == ry[t]
    end
    return num_correct.to_f / num_data
  end
end



if __FILE__ == $0
  cv, y = knock72
  x = cv.doc_matrix

  x_train, y_train, x_test, y_test = CrossValidation.train_test_split(x, y, 0.7).map(&:dup)

  model = LogisticRegressionModel.new
  model.fit(x_train, y_train)

  puts "test accuracy: #{model.score(x_test, y_test)}"
end
