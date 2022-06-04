# 7 kyu
# White or Black?

def square_color(file, rank):
    if (file in 'aceg' and rank % 2 == 0) or (file in 'bdfh' and rank % 2 != 0):
        return 'white'
    return 'black'


print(square_color("a", 8), "white")
print(square_color("b", 2), "black")
print(square_color("f", 5), "white")
