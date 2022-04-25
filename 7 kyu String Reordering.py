def sentence(List):
    lst = []
    for i in List:
        for j in i.keys():
            j = int(j)

    for i in List:
        print(i)

List = [
    {'4': 'dog'}, {'2': 'took'}, {'3': 'his'},
    {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
]

print(sentence(List), 'Vatsan took his dog for a spin')
