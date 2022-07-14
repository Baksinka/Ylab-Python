from abc import ABC, abstractmethod

from antagonistfinder import AntagonistFinder
from weapons import Gun, Kick, Lasers


class SuperHero(ABC):
    name = ''
    can_use_ultimate_attack = False
    finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    @abstractmethod
    def attack(self):
        ...


class Superman(SuperHero):
    name = 'Clark Kent'
    can_use_ultimate_attack = True

    def attack(self):
        Kick().kick()

    def ultimate(self):
        Lasers().incinerate_with_lasers()


class ChackNorris(SuperHero):
    name = 'Chack Norris'

    def attack(self):
        Gun().fire_a_gun()
