def life_path_number(s):
    return int(s.replace("-", "")) % 9 or 9


print(life_path_number("1955-10-28"), 4)
print(life_path_number("1971-06-28"), 7)
