from enum import Enum

from attrs import define


class Suit(Enum):
    DOT = 1
    STICK = 2
    CHARACTER = 3
    WIND = 4
    DRAGON = 5
    SEASON = 6
    FLOWER = 7


@define
class Tile:
    suit: str
    name: str
    value: int

    @property
    def is_numeric(self):
        return self.suit in {Suit.DOT, Suit.STICK, Suit.CHARACTER}

    @property
    def is_wind(self):
        return self.suit == Suit.WIND

    @property
    def is_dragon(self):
        return self.suit == Suit.DRAGON

    @property
    def is_flower(self):
        return self.suit in {Suit.SEASON, Suit.FLOWER}

    def __lt__(self, obj):
        return (self.suit.value, self.value) < (obj.suit.value, obj.value)

    def __eq__(self, obj):
        return self.suit == obj.suit and self.value == obj.value

    def __repr__(self):
        return f'{self.suit.name}_{self.name}'


TILES = [
    Tile(Suit.DOT, '1', 1),
    Tile(Suit.DOT, '2', 2),
    Tile(Suit.DOT, '3', 3),
    Tile(Suit.DOT, '4', 4),
    Tile(Suit.DOT, '5', 5),
    Tile(Suit.DOT, '6', 6),
    Tile(Suit.DOT, '7', 7),
    Tile(Suit.DOT, '8', 8),
    Tile(Suit.DOT, '9', 9),
    Tile(Suit.STICK, '1', 1),
    Tile(Suit.STICK, '2', 2),
    Tile(Suit.STICK, '3', 3),
    Tile(Suit.STICK, '4', 4),
    Tile(Suit.STICK, '5', 5),
    Tile(Suit.STICK, '6', 6),
    Tile(Suit.STICK, '7', 7),
    Tile(Suit.STICK, '8', 8),
    Tile(Suit.STICK, '9', 9),
    Tile(Suit.CHARACTER, '1', 1),
    Tile(Suit.CHARACTER, '2', 2),
    Tile(Suit.CHARACTER, '3', 3),
    Tile(Suit.CHARACTER, '4', 4),
    Tile(Suit.CHARACTER, '5', 5),
    Tile(Suit.CHARACTER, '6', 6),
    Tile(Suit.CHARACTER, '7', 7),
    Tile(Suit.CHARACTER, '8', 8),
    Tile(Suit.CHARACTER, '9', 9),
    Tile(Suit.WIND, 'EAST', 0),
    Tile(Suit.WIND, 'SOUTH', 1),
    Tile(Suit.WIND, 'WEST', 2),
    Tile(Suit.WIND, 'NORTH', 3),
    Tile(Suit.DRAGON, 'RED', 0),
    Tile(Suit.DRAGON, 'GREEN', 1),
    Tile(Suit.DRAGON, 'WHITE', 2),
]

FLOWER_TILES = [
    Tile(Suit.SEASON, '1', 1),
    Tile(Suit.SEASON, '2', 2),
    Tile(Suit.SEASON, '3', 3),
    Tile(Suit.SEASON, '4', 4),
    Tile(Suit.FLOWER, '1', 1),
    Tile(Suit.FLOWER, '2', 2),
    Tile(Suit.FLOWER, '3', 3),
    Tile(Suit.FLOWER, '4', 4),
]

