"""Effect for Galakrond, the Unbreakable (DRG_650).

Card Text: [x]<b>Battlecry:</b> Draw 1 minion.
Give it +4/+4.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)