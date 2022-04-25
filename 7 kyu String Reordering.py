def sentence(lst):
    return sorted(lst)


def sentence(input):
    pairs = [list(*x.items()) for x in input]
    ordered = sorted(pairs, key=lambda k: int(k[0]))
    return ' '.join(word for i, word in ordered)


List = [
    {'4': 'dog'}, {'2': 'took'}, {'3': 'his'},
    {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
]

print(sentence(List), 'Vatsan took his dog for a spin')
