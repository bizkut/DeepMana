"""Effect for Shield of Galakrond (DRG_242).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> <b>Invoke</b> Galakrond.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass