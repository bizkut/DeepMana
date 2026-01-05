"""Effect for Hero's Welcome (DINO_424).

Card Text: <b>Discover</b> a <b>Legendary</b> minion to summon. Set its stats to 10/10.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DINO_424t")