"""Effect for Coldlight Seer (EX1_103).

Card Text: <b>Battlecry:</b> Give your other Murlocs +2 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)