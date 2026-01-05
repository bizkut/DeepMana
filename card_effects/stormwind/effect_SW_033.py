"""Effect for Canal Slogger (SW_033).

Card Text: <b>Rush</b>, <b>Lifesteal</b>
<b>Overload:</b> (1)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass