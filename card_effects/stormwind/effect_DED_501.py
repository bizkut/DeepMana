"""Effect for Sunwing Squawker (DED_501).

Card Text: [x]<b>Battlecry:</b> Repeat the last
spell you've cast on a
  friendly minion on this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass