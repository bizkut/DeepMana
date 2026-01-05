"""Effect for Soldier of the Bronze (TIME_720).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Double this minion's Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)