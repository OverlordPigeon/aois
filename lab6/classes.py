class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash_function(self, key):
        return hash(key) % self.capacity

    def add(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = Node(key, value)
                print(f"Обнаружена коллизия для ключа: {key}")

    def get(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Ключ '{key}' не найден")

    def remove(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return
            previous = current
            current = current.next
        raise KeyError(f"Ключ '{key}' не найден")

    def __str__(self):
        items = []
        for idx, node in enumerate(self.table):
            current = node
            while current:
                items.append(f"Индекс: {idx}, Ключ: {current.key}, Значение: {current.value}")
                current = current.next
        return "\n".join(items)