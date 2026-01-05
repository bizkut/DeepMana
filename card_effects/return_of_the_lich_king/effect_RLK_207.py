"""Effect for Fierce Outsider (RLK_207).

Card Text: <b>Rush</b>
<b>Outcast:</b> Your next <b>Outcast</b> card costs (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass