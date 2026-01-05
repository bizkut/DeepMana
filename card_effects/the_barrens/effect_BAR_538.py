"""Effect for Druid of the Plains (BAR_538).

Card Text: <b>Rush</b>
<b>Frenzy:</b> Transform into a 6/7 Kodo with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass