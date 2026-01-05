"""Effect for Spirit Lash (ICC_802).

Card Text: <b>Lifesteal</b>
Deal $1 damage to all minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)