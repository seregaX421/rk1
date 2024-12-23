class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)
            comp_item = item
            if self.ignore_case and isinstance(item, str):
                comp_item = item.lower()
            if comp_item not in self.seen:
                self.seen.add(comp_item)
                return item

    def __iter__(self):
        return self
