class FlatIterator:
    def __init__(self, lst):
        self.lst = lst
        self.cursor = -1
        self.list_len = len(self.lst)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self.lst[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.nest_cursor += 1
        return self.lst[self.cursor][self.nest_cursor - 1]


def mygen(lst):
    for items in lst:
        for item in items:
            yield item


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    print("______________________")
    for item in mygen(nested_list):
        print(item)
