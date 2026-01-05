"""Effect for Sunborne Val'kyr (ICC_028).

Card Text: <b>Battlecry:</b> Give adjacent minions +2 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)