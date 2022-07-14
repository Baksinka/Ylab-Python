from abc import ABC, abstractmethod


class Alert(ABC):

    @abstractmethod
    def create_news(self, place, hero):
        ...


class TV(Alert):

    def create_news(self, place, hero):
        place_name = getattr(place, 'name', 'place')
        hero_name = getattr(hero, 'name', 'hero')
        print(f'{hero_name} saved the {place_name}!')


class NewsPlanet(Alert):

    def create_news(self, place, hero):
        place_coord = getattr(place, 'coordinates', 'place')
        hero_name = getattr(hero, 'name', 'hero')
        print(f'{hero_name} saved the {place_coord}!')
