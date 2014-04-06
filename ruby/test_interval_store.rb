#ruby-2.0.0-p247

require_relative 'interval_store'
require "test/unit"


# > store = IntervalStore.new
# []
# > store.add(1, 2)
# [[1, 2]]
# > store.add(5, 6)
# [[1, 2], [5, 6]]
# > store.add(1, 4)
# [[1, 4], [5, 6]]
# > store.add(1, 2)
# [[1, 4], [5, 6]]
# > store.add(3, 5)
# [[1, 6]]
# > store.add(0, 7)
# [[0, 7]]
##

class TestIntervalStore < Test::Unit::TestCase
  def test_should_not_merge_if_no_intersection
    store = IntervalStore.new
    store.add(1, 2)
    store.add(5, 6)
    assert_equal([[1, 2], [5, 6]].to_s, store.to_s)
  end

  def test_should_merge_if_two_number_both_appearance
    store = IntervalStore.new
    store.add(1, 2)
    store.add(5, 6)
    store.add(7, 8)
    store.add(5, 7)
    assert_equal([[1, 2], [5, 8]].to_s, store.to_s)
  end

  def test_should_merge_if_only_low_number_appearance_and_upp_number_is_not_between_any_exist_interval
    store = IntervalStore.new
    store.add(1, 2)
    store.add(5, 6)
    store.add(1, 4)
    assert_equal([[1, 4], [5, 6]].to_s, store.to_s)
  end

  def test_should_merge_if_only_low_number_appearance_and_upp_number_is_between_any_exist_interval
    store = IntervalStore.new
    store.add(1, 2)
    store.add(5, 6)
    store.add(1, 4)
    store.add(1, 2)
    assert_equal([[1, 4], [5, 6]].to_s, store.to_s)
  end

  def test_should_merge_if_only_upp_number_appearance_and_low_number_is_not_between_any_exist_interval
    store = IntervalStore.new
    store.add(1, 2)
    store.add(5, 6)
    store.add(1, 4)
    store.add(0, 5)
    assert_equal([[0, 6]].to_s, store.to_s)
  end

  def test_should_merge_if_only_upp_number_appearance_and_low_number_is_between_any_exist_interval
    store = IntervalStore.new
    store.add(1, 2)
    store.add(5, 6)
    store.add(1, 4)
    store.add(3, 5)
    assert_equal([[1, 6]].to_s, store.to_s)
  end

  def test_should_merge_if_neither_upp_number_nor_low_number_is_appearance
    store = IntervalStore.new
    store.add(1, 2)
    store.add(5, 6)
    store.add(1, 4)
    store.add(1, 2)
    store.add(3, 5)
    store.add(0, 7)
    assert_equal([[0, 7]].to_s, store.to_s)
  end
end