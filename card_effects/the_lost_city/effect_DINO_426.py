"""Effect for Ritual of Life (DINO_426).

Card Text: <b>Discover</b> a 3-Cost minion. Summon a 2/3 copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DINO_426t")