"""Effect for Stowaway (DRG_034).

Card Text: [x]<b>Battlecry:</b> If there are cards
in your deck that didn't start
there, draw 2 of them.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)