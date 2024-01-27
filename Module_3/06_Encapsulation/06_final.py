class Counter:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


c = Counter(5)

for i in c:
    print(i)
