class IntervalStore

  def initialize
    @store = []
  end

  def to_s
    "[#{@store.map{ |i| "[#{i.first}, #{i.last}]" }.join(', ')}]"
  end

  # TODO - implement this method
  def add(low, upp)
    flatten_store = @store.flatten

    low_index, upp_index = flatten_store.index(low), flatten_store.index(upp)
    if low_index and upp_index
      low_index -=1 if low_index.odd?
      upp_index +=1 if upp_index.even?
    elsif low_index and !upp_index
      low_index -= 1 if low_index.odd?
      (flatten_store << upp).sort!
      upp_index = flatten_store.index(upp)
      upp_index += 1 if upp_index.odd?
    elsif !low_index and upp_index
      upp_index += 1 if upp_index.even?
      (flatten_store << low).sort!
      low_index = flatten_store.index(low)
      low_index -= 1 if low_index.odd?
      upp_index += 1
    else
      (flatten_store << low << upp).sort!
      low_index, upp_index = flatten_store.index(low), flatten_store.index(upp)

      low_index -= 1 if low_index.odd?
      upp_index += 1 if upp_index.even?
    end

    filter_result = filter_store(flatten_store, low_index, upp_index)
    format_result(filter_result)
  end

  def format_result(rest)
    @store = []
    rest.each_slice(2) { |pair_values| @store << pair_values }
  end

  def filter_store(flatten_store, low_index, upp_index)
    flatten_store.clone.delete_if do |value|
      flatten_store_index = flatten_store.index(value)
      low_index < flatten_store_index and flatten_store_index < upp_index
    end
  end
end
