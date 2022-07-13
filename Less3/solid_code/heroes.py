from antagonistfinder import AntagonistFinder
from weapons import Gun, Kick, Lasers


class SuperHero(Gun):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        self.fire_a_gun()


class Superman(SuperHero, Lasers, Kick):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        self.kick()

    def ultimate(self):
        self.incinerate_with_lasers()
