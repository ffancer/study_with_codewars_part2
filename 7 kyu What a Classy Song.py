# 7 kyu
# What a "Classy" Song


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = set()

    def how_many(self, listeners_today):
        cnt = 0

        for i in listeners_today:
            if i.lower() not in self.listeners:
                cnt += 1
                self.listeners += i.lower()

        return cnt


mount_moose = Song('Mount Moose', 'The Snazzy Moose')
print(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn']), 5)
print(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']), 2)
print(mount_moose.how_many(['Amanda', 'CalEb', 'CarL', 'Furgus']), 2)
print(mount_moose.how_many(['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE']), 1)
