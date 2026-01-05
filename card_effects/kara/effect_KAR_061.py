"""Effect for The Curator (KAR_061).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Draw a Beast, Dragon, and Murloc from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)