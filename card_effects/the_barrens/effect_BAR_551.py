"""Effect for Barak Kodobane (BAR_551).

Card Text: [x]<b>Battlecry:</b> Draw a 1, 2,
  and 3-Cost spell.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)