"""Effect for Scrapsmith (AV_323).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Add two 2/4 Grunts with <b>Taunt</b> to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass