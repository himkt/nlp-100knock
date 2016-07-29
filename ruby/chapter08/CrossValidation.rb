module CrossValidation

  # x, y: Narray object
  # We slice a matrix by x[Array<Integer>, true]
  def self.train_test_split(x, y, test_size=0.33)
    doc_size = x.shape[0]
    random_indices = (0...doc_size).to_a.shuffle
    endpoint = (doc_size * test_size).to_i
    train_indices = random_indices[0...endpoint]
    test_indices = random_indices[endpoint..-1]

    return [x[train_indices, true], y[train_indices, true], y[test_indices, true], y[test_indices, true]]
  end

  class KFold
    def initialize(n, n_folds, shuffle)
      indices = (0...n).to_a
      indices.shuffle! if shuffle

      @indices = indices
      @n_folds = n_folds
    end

    def create
      groups_nfolds = @indices.each_slice((@indices.size.to_f / @n_folds).ceil).to_a
      groups = []

      @n_folds.times do |k|
        validation_set = []
        test_set = []

        @n_folds.times do |j|
          test_set += groups_nfolds[j] if k == j
          validation_set += groups_nfolds[j] unless k == j
        end

        groups << [validation_set, test_set]
      end

      return groups
    end
  end
end
