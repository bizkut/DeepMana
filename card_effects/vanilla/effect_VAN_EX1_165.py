"""Effect for Druid of the Claw (VAN_EX1_165).

Card Text: <b>Choose One -</b> <b>Charge</b>; or +2 Health and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)