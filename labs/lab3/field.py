goods = [
    {'title': 'Телевизор', 'price': 30000, 'color': 'black'},
    {'title': 'Кирилл', 'price': 41, 'color': 'black'}
]


def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            sp = {key: item.get(key) for key in args if item.get(key) is not None}
            yield sp


print(list(field(goods, 'title', 'color')))