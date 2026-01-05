"""Effect for Champions of Azeroth (WON_113).

Card Text: [x]Choose Alliance or Horde.
Get 2 of their <b>Legendary</b>
Champions and reduce
their Costs by (2).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass