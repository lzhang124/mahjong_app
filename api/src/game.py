import random

from attrs import define, Factory

from .tile import TILES, FLOWER_TILES, Tile


N_PLAYERS = 4


@define
class Game:
    players: list
    min_points: int = 8
    include_flowers: bool = True
    play_order: list = Factory(lambda: list(range(N_PLAYERS)))
    dealer_i: int = 0
    current_i: int = 0
    start: int = 0
    tiles: list = Factory(list)

    @classmethod
    def with_players(cls, players):
        return cls([Player(p) for p in players])

    @property
    def players_in_order(self):
        return [self.players[self.play_order[(self.dealer_i + i) % 4]] for i in range(N_PLAYERS)]

    @property
    def dealer(self):
        return self.players[self.play_order[self.dealer_i]]

    def new_game(self):
        self._shuffle_play_order()
        self.new_round()

    def new_round(self):
        for p in self.players:
            p.reset()
        self.current_i = self.dealer_i
        self._deal()

    def _shuffle_play_order(self):
        random.shuffle(self.play_order)

    def _shuffle_tiles(self):
        self.tiles = [tile for tile in TILES for _ in range(4)]
        if self.include_flowers:
            self.tiles.extend(FLOWER_TILES)
        random.shuffle(self.tiles)

    def _next_player(self):
        self.current_i = (self.current_i + 1) % 4

    def _draw_hand(self, player, n):
        player.draw_hand(self.tiles[:n])
        self.tiles = self.tiles[n:]

    def _draw(self, player):
        while player.drawn_tile is None:
            player.draw(self.tiles[0])
            self.tiles = self.tiles[1:]

    def _deal(self):
        self._shuffle_tiles()
        n_tiles = len(self.tiles)
        first = random.randint(1, 6) + random.randint(1, 6)
        second = random.randint(1, 6) + random.randint(1, 6)
        wall = (first - 1) % 4
        self.start = (wall * (n_tiles // 4) + (first + second) * 2) % n_tiles
        self.tiles = self.tiles[self.start:] + self.tiles[:self.start]

        for _ in range(3):
            for p in self.players_in_order:
                self._draw_hand(p, 4)
        for p in self.players_in_order:
            self._draw_hand(p, 1)
        self._draw_hand(self.dealer, 1)

        if self.include_flowers:
            num_flowers = [p.num_flowers() for p in self.players_in_order]
            while sum(num_flowers) > 0:
                for i, p in enumerate(self.players_in_order):
                    p.reveal_flowers()
                    self._draw_hand(p, num_flowers[i])
                    num_flowers[i] = p.num_flowers()

        self.dealer.drawn_tile = self.dealer.hidden.pop()

        for p in self.players_in_order:
            p.sort()


@define
class Player:
    name: str
    hidden: list = Factory(list)
    visible: list = Factory(list)
    flowers: list = Factory(list)
    discard: list = Factory(list)
    drawn_tile: Tile = None
    scores: list = Factory(list)

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
