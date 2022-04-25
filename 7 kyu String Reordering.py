def sentence(ds):
    return ' '.join(v for _, v in sorted((int(k), v) for d in ds for k, v in d.items()))

List = [
    {'4': 'dog'}, {'2': 'took'}, {'3': 'his'},
    {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
]

print(sentence(List), 'Vatsan took his dog for a spin')
