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
end
