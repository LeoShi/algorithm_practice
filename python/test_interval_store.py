from unittest import TestCase, main
from interval_store import IntervalStore


class TestIntervalStore(TestCase):
    def test_should_not_merge_if_no_intersection(self):
        store = IntervalStore()
        store.add(1, 2)
        store.add(5, 6)
        self.assertEqual([[1, 2], [5, 6]], store.store)

    def test_should_merge_if_two_number_both_appearance(self):
        store = IntervalStore()
        store.add(1, 2)
        store.add(5, 6)
        store.add(7, 8)
        store.add(5, 7)
        self.assertEqual([[1, 2], [5, 8]], store.store)
    
    def test_should_merge_if_only_low_number_appearance_and_upp_number_is_not_between_any_exist_interval(self):
        store = IntervalStore()
        store.add(1, 2)
        store.add(5, 6)
        store.add(1, 4)
        self.assertEqual([[1, 4], [5, 6]], store.store)
    
    def test_should_merge_if_only_low_number_appearance_and_upp_number_is_between_any_exist_interval(self):
        store = IntervalStore()
        store.add(1, 2)
        store.add(5, 6)
        store.add(1, 4)
        store.add(1, 2)
        self.assertEqual([[1, 4], [5, 6]], store.store)
    
    def test_should_merge_if_only_upp_number_appearance_and_low_number_is_not_between_any_exist_interval(self):
        store = IntervalStore()
        store.add(1, 2)
        store.add(5, 6)
        store.add(1, 4)
        store.add(0, 5)
        self.assertEqual([[0, 6]], store.store)
    
    def test_should_merge_if_only_upp_number_appearance_and_low_number_is_between_any_exist_interval(self):
        store = IntervalStore()
        store.add(1, 2)
        store.add(5, 6)
        store.add(1, 4)
        store.add(3, 5)
        self.assertEqual([[1, 6]], store.store)
    
    def test_should_merge_if_neither_upp_number_nor_low_number_is_appearance(self):
        store = IntervalStore()
        store.add(1, 2)
        store.add(5, 6)
        store.add(1, 4)
        store.add(1, 2)
        store.add(3, 5)
        store.add(0, 7)
        self.assertEqual([[0, 7]], store.store)


if __name__ == '__main__':
    main()
