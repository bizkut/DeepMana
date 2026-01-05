"""Effect for Witch's Apprentice (GIL_531).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Add a random Shaman spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass