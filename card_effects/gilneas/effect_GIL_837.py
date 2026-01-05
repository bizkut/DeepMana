"""Effect for Glitter Moth (GIL_837).

Card Text: <b>Battlecry:</b> If your deck has only odd-Cost cards, double the Health of your other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)