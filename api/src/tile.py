from enum import Enum

from attrs import define
from sqlalchemy.types import TypeDecorator, Text


class Suit(Enum):
    DOT = 1
    STICK = 2
    CHARACTER = 3
    WIND = 4
    DRAGON = 5
    SEASON = 6
    FLOWER = 7

    @property
    def is_numeric(self):
        return self.name in {'DOT', 'STICK', 'CHARACTER'}

    @property
    def is_wind(self):
        return self.name == 'WIND'

    @property
    def is_dragon(self):
        return self.name == 'DRAGON'

    @property
    def is_flower(self):
        return self.name in {'SEASON', 'FLOWER'}


class Wind(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


class Dragon(Enum):
    RED = 1
    GREEN = 2
    WHITE = 3


@define
class Tile:
    suit: Suit
    value: int

    @classmethod
    def from_string(cls, string):
        s, v = string.split('_')
        suit = Suit[s]
        if suit.is_wind:
            value = Wind[v].value
        elif suit.is_dragon:
            value = Dragon[v].value
        else:
            value = int(v)
        return cls(suit, value)

    @property
    def is_numeric(self):
        return self.suit.is_numeric

    @property
    def is_wind(self):
        return self.suit.is_wind

    @property
    def is_dragon(self):
        return self.suit.is_dragon

    @property
    def is_flower(self):
        return self.suit.is_flower

    @property
    def name(self):
        if self.suit.is_wind:
            value = Wind(self.value).name
        elif self.suit.is_dragon:
            value = Dragon(self.value).name
        else:
            value = str(self.value)
        return f'{self.suit.name}_{value}'

    def __lt__(self, obj):
        return (self.suit.value, self.value) < (obj.suit.value, obj.value)

    def __eq__(self, obj):
        return self.suit == obj.suit and self.value == obj.value

    def __repr__(self):
        return self.name


class TileType(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        return value.name

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        else:
            return Tile.from_string(value)


TILES = [
    Tile(Suit.DOT, 1),
    Tile(Suit.DOT, 2),
    Tile(Suit.DOT, 3),
    Tile(Suit.DOT, 4),
    Tile(Suit.DOT, 5),
    Tile(Suit.DOT, 6),
    Tile(Suit.DOT, 7),
    Tile(Suit.DOT, 8),
    Tile(Suit.DOT, 9),
    Tile(Suit.STICK, 1),
    Tile(Suit.STICK, 2),
    Tile(Suit.STICK, 3),
    Tile(Suit.STICK, 4),
    Tile(Suit.STICK, 5),
    Tile(Suit.STICK, 6),
    Tile(Suit.STICK, 7),
    Tile(Suit.STICK, 8),
    Tile(Suit.STICK, 9),
    Tile(Suit.CHARACTER, 1),
    Tile(Suit.CHARACTER, 2),
    Tile(Suit.CHARACTER, 3),
    Tile(Suit.CHARACTER, 4),
    Tile(Suit.CHARACTER, 5),
    Tile(Suit.CHARACTER, 6),
    Tile(Suit.CHARACTER, 7),
    Tile(Suit.CHARACTER, 8),
    Tile(Suit.CHARACTER, 9),
    Tile(Suit.WIND, 0),
    Tile(Suit.WIND, 1),
    Tile(Suit.WIND, 2),
    Tile(Suit.WIND, 3),
    Tile(Suit.DRAGON, 1),
    Tile(Suit.DRAGON, 2),
    Tile(Suit.DRAGON, 3),
]

FLOWER_TILES = [
    Tile(Suit.SEASON, 1),
    Tile(Suit.SEASON, 2),
    Tile(Suit.SEASON, 3),
    Tile(Suit.SEASON, 4),
    Tile(Suit.FLOWER, 1),
    Tile(Suit.FLOWER, 2),
    Tile(Suit.FLOWER, 3),
    Tile(Suit.FLOWER, 4),
]

