"""Effect for Ancient of Yore (EDR_979).

Card Text: [x]<b>Dormant</b> for 2 turns.
While <b>Dormant</b>, gain 3
Armor and draw a card at
the end of your turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)