class Water:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Wind):
            return Storm.name(self)
        elif isinstance(other, Fire):
            return Steam.name(self)
        elif isinstance(other, Earth):
            return Dirt.name(self)


class Wind:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm.name(self)
        elif isinstance(other, Fire):
            return Ligthing.name(self)
        elif isinstance(other, Earth):
            return Dust.name(self)


class Fire:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam.name(self)
        elif isinstance(other, Wind):
            return Ligthing.name(self)
        elif isinstance(other, Earth):
            return Magma.name(self)


class Earth:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt.name(self)
        elif isinstance(other, Wind):
            return Dust.name(self)
        elif isinstance(other, Earth):
            return Magma.name(self)


class Light:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Water):
            return Mist.name(self)
        elif isinstance(other, Wind):
            return Mirage.name(self)
        elif isinstance(other, Earth):
            return Meteorite.name(self)
        elif isinstance(other, Fire):
            return Plasma.name(self)


class Mist:

    def name(self):
        name = 'Туман'
        return name


class Mirage:

    def name(self):
        name = 'Иллюзия'
        return name


class Meteorite:

    def name(self):
        name = 'Метеорит'
        return name


class Plasma:

    def name(self):
        name = 'Плазма'
        return name


class Storm:

    def name(self):
        name = 'Шторм'
        return name


class Ligthing:

    def name(self):
        name = 'Молния'
        return name

class Dust:

    def name(self):
        name = 'Пыль'
        return name

class Steam:

    def name(self):
        name = 'Пар'
        return name


class Dirt:

    def name(self):
        name = 'Грязь'
        return name


class Magma:

    def name(self):
        name = 'Лава'
        return name


water = Water('Вода')
wind = Wind('Воздух')
fire = Fire('Огонь')
earth = Earth('Земля')
ligth = Light('Свет')
storm = water + wind
steam = water + fire
dirt = water + earth
ligthing = wind + fire
dust = wind + earth
magma = fire + earth
mist = ligth + water
mirage = ligth + wind
meteorite = ligth + earth
plasma = ligth + fire
print('Если соединить элемент {water} и элемент {wind} мы получим новый элемент: {storm}!'.format(water=water.name,
                                                                                           wind=wind.name,storm=storm))
print('Если соединить элемент {water} и элемент {fire} мы получим новый элемент: {steam}!'.format(water=water.name,
                                                                                           fire=fire.name,steam=steam))
print('Если соединить элемент {water} и элемент {earth} мы получим новый элемент: {dirt}!'.format(water=water.name,
                                                                                           earth=earth.name,dirt=dirt))
print('Если соединить элемент {wind} и элемент {fire} мы получим новый элемент: {ligthing}!'.format
      (wind=wind.name,fire=fire.name,ligthing=ligthing))
print('Если соединить элемент {wind} и элемент {earth} мы получим новый элемент: {dust}!'.format
      (wind=wind.name,earth=earth.name,dust=dust))
print('Если соединить элемент {fire} и элемент {earth} мы получим новый элемент: {magma}!'.format
      (fire=fire.name,earth=earth.name,magma=magma))
print('Если соединить элемент {light} и элемент {water} мы получим новый элемент: {mist}!'.format
      (light=ligth.name,water=water.name,mist=mist))
print('Если соединить элемент {light} и элемент {wind} мы получим новый элемент: {mirage}!'.format
      (light=ligth.name,wind=wind.name,mirage=mirage))
print('Если соединить элемент {light} и элемент {earth} мы получим новый элемент: {meteorite}!'.format
      (light=ligth.name,earth=earth.name,meteorite=meteorite))
print('Если соединить элемент {light} и элемент {fire} мы получим новый элемент: {plasma}!'.format
      (light=ligth.name,fire=fire.name,plasma=plasma))