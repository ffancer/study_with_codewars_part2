class Marine:
    def __init__(self):
        self.health = 100

    def accept(self, visitor):
        return visitor.visit_light(self)


class Marauder:
    def __init__(self):
        self.health = 125

    def accept(self, visitor):
        return visitor.visit_armored(self)


class TankBullet:
    def visit_light(self, unit):
        unit.health -= 21

    def visit_armored(self, unit):
        unit.health -= 32


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
