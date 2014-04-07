class IntervalStore

  def initialize
    @store = []
  end

  def to_s
    "[#{@store.map{ |i| "[#{i.first}, #{i.last}]" }.join(', ')}]"
  end

  # TODO - implement this method
  def add(low, upp)
    @store << [low, upp]
    @store.sort_by!(&:first)
    result = []
    @store.each do |interval|
      if result.empty?
        result << interval
      else
        last_interval = result.pop
        if last_interval.last < interval.first
          result << last_interval << interval
        else
          min_value, max_value = [last_interval.first, interval.first, last_interval.last, interval.last].minmax
          result << [min_value, max_value]
        end
      end
    end
    @store = result
  end
end
