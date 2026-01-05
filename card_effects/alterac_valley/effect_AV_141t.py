"""Effect for Lokholar the Ice Lord (AV_141t).

Card Text: <b>Rush</b>, <b>Windfury</b>
 Costs (5) less if you have 15 Health or less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 5, source)