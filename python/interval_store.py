class IntervalStore(object):
    def __init__(self):
        self.store = []

    def filter_result(self, flatten_store, low_index, upp_index):
        useless_values = filter(lambda value: low_index < flatten_store.index(value) < upp_index, flatten_store)
        flatten_store = filter(lambda value: value not in useless_values, flatten_store)
        self.store = []
        for i, k in zip(flatten_store[0::2], flatten_store[1::2]):
            self.store.append([i, k])

    def add(self, low, upp):
        flatten_store = [number for pair in self.store for number in pair]
        low_index, upp_index = self.index_of(low, flatten_store), self.index_of(upp, flatten_store)

        if low_index >= 0 and upp_index >= 0:
            if low_index % 2 != 0:
                low_index -= 1
            if upp_index % 2 == 0:
                upp_index += 1
        elif low_index >= 0 > upp_index:
            if low_index % 2 != 0:
                low_index -= 1
            flatten_store.append(upp)
            flatten_store = sorted(flatten_store)
            upp_index = self.index_of(upp, flatten_store)
            if upp_index % 2 != 0:
                upp_index += 1
        elif low_index < 0 <= upp_index:
            if upp_index % 2 == 0:
                upp_index += 1
            flatten_store.append(low)
            flatten_store = sorted(flatten_store)
            low_index = self.index_of(low, flatten_store)
            if low_index % 2 != 0:
                low_index -= 1
            upp_index += 1
        else:
            flatten_store.append(low)
            flatten_store.append(upp)
            flatten_store = sorted(flatten_store)
            low_index, upp_index = self.index_of(low, flatten_store), self.index_of(upp, flatten_store)

            if low_index % 2 != 0:
                low_index -= 1
            if upp_index % 2 == 0:
                upp_index += 1
        self.filter_result(flatten_store, low_index, upp_index)

    def index_of(self, value, list):
        try:
            return list.index(value)
        except ValueError:
            return -1


