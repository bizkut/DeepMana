"""Effect for Ancient of Lore (CORE_NEW1_008).

Card Text: <b>Choose One -</b> Draw 2 cards; or Restore #7 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)