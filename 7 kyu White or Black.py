# 7 kyu
# White or Black?

def square_color(file, rank):
    return 'white' if (ord(file) + rank) % 2 else 'black'


print(square_color("a", 8), "white")
print(square_color("b", 2), "black")
print(square_color("f", 5), "white")
