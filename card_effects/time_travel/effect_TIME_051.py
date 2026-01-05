"""Effect for Soldier of the Infinite (TIME_051).

Card Text: <b>Rush</b>
<b>Battlecry:</b> Double this minion's Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass