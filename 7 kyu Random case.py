def random_case(x):
    pass


v = [
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
  "Donec eleifend cursus lobortis",
  "THIS IS AN ALL CAPS STRING",
  "this is an all lower string"
]


for i in v:
  r = random_case(i)
  # print(r.lower(), i.lower())
  print(r, i)
  print(r, i.upper())
  print(r, i.lower())