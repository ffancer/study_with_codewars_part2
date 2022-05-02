class Marine:
    def __init__(self):
        pass

    def accept(self, visitor):
        pass


class Marauder:
    def __init__(self):
        pass

    def accept(self, visitor):
        pass


class TankBullet:
    def visit_light(self, unit):
        pass

    def visit_armored(self, unit):
        pass


print('Visit Light')
bullet = TankBullet()
light = Marine()
light.accept(bullet)
print(light.health, 100 - 21)

print('Visit Armored')
bullet = TankBullet()
armored = Marauder()
armored.accept(bullet)
print(armored.health, 125 - 32)
