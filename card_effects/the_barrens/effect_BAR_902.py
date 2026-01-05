"""Effect for Cariel Roame (BAR_902).

Card Text: [x]<b>Rush</b>, <b>Divine Shield</b>
Whenever this attacks,
reduce the Cost of Holy
      spells in your hand by (1).   
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass