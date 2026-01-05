"""Effect for Sunkeeper Tarim (UNG_015).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Set all other minions' Attack and Health to 3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)