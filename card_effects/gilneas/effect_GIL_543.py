"""Effect for Dark Possession (GIL_543).

Card Text: Deal $2 damage to a friendly character. <b>Discover</b> a Demon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)