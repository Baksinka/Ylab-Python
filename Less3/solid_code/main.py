from typing import Union

from alert import TV, Alert
from heroes import SuperHero, Superman
from places import Kostroma, Tokyo


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo], alert: Alert):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    alert.create_news(place, hero)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), TV())
    print('-' * 20)
    save_the_place(SuperHero('Chack Norris', False), Tokyo(), TV())
