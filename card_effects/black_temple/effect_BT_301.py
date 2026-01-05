"""Effect for Nightshade Matron (BT_301).

Card Text: <b>Rush</b>
<b>Battlecry:</b> Discard your highest Cost card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass