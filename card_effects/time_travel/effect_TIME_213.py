"""Effect for Primordial Overseer (TIME_213).

Card Text: [x]<b>Battlecry:</b> If you've cast a
Nature spell while holding
this, gain +1/+1 and
draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)