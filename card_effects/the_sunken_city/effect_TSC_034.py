"""Effect for Gorloc Ravager (TSC_034).

Card Text: [x]<b>Battlecry:</b> Draw 3 Murlocs.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)