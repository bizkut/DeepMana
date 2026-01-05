"""Effect for Hot Spring Guardian (UNG_938).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Restore #3 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)