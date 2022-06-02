class List:
    def __init__(self, type):
        self.type = type
        self.items = []
        self.count = 0

    def add(self, item):
        if not isinstance(item, self.type):
            return f"This item is not of type: {self.type.__name__}"
        self.items.append(item)
        self.count += 1
        return self


my_list = List(str)

print(my_list.add('Hello').count, 1, 'How many items in the List?')
print(my_list.add(5), "This item is not of type: str", 'Wrong type added')
print(my_list.add(' ').add('World!').count, 3, 'How many items in the List?')
