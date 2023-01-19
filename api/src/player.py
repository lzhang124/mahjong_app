from sqlalchemy import Column, Text, ARRAY

from .db import Base
from .tile import TileType


class Player(Base):
    name = Column(Text, nullable=False)
    hidden = Column(ARRAY(Text), server_default='{}')
    visible = Column(ARRAY(Text), server_default='{}')
    flowers = Column(ARRAY(Text), server_default='{}')
    discard = Column(ARRAY(Text), server_default='{}')
    drawn_tile = Column(TileType, nullable=True)

    def reset(self):
        self.hidden = []
        self.visible = []
        self.flowers = []
        self.discard = []

    def draw_hand(self, tiles):
        self.hidden.extend(tiles)

    def draw(self, tile):
        if tile.is_flower:
            self.flowers.append(tile)
        else:
            self.drawn_tile = tile

    def sort(self):
        self.hidden.sort()

    def num_flowers(self):
        return sum(1 for t in self.hidden if t.is_flower)

    def reveal_flowers(self):
        self.flowers.extend(t for t in self.hidden if t.is_flower)
        self.hidden = [t for t in self.hidden if not t.is_flower]

    def __repr__(self):
        return f'<Player id:{self.id} name:{self.name}>'
