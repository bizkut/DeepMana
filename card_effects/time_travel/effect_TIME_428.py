"""Effect for Yesterloc (TIME_428).

Card Text: At the end of your turn, give your other minions +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)