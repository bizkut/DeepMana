"""Effect for Ancient of Lore (VAN_NEW1_008).

Card Text: <b>Choose One -</b> Draw 2 cards; or Restore #5 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)