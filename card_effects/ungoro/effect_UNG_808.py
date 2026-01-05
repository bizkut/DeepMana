"""Effect for Stubborn Gastropod (UNG_808).

Card Text: <b>Taunt</b>
  <b>Poisonous</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass