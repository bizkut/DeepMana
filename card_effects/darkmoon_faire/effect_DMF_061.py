"""Effect for Faire Arborist (DMF_061).

Card Text: [x]<b>Choose One - </b>Draw a card;
or Summon a 2/2 Treant.
<b>Corrupt:</b> Do both.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)