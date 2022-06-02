class List:
    def __init__(self, type):
        self.type = type
        self.items = []
        self.count = 0

    def add(self, item):
        if type(item) != self.type:
            item_type = "str" if self.type == str else "int" if self.type == int else "float"
            return "This item is not of type: %s" % (item_type)
        self.items += [item]
        self.count += 1
        return item


my_list = List(str)

print(my_list.add('Hello').count, 1, 'How many items in the List?')
print(my_list.add(5), "This item is not of type: str", 'Wrong type added')
print(my_list.add(' ').add('World!').count, 3, 'How many items in the List?')