from abc import ABC, abstractmethod


class Place(ABC):

    @abstractmethod
    def find_antagonist(self):
        ...


class Kostroma(Place):
    name = 'Kostroma'

    def find_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def find_antagonist(self):
        print('Godzilla stands near a skyscraper')
