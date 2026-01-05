"""Effect for Petal Picker (FIR_921).

Card Text: [x]<b>Battlecry:</b> If you've <b>Imbued</b>
your Hero Power twice,
draw 2 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)