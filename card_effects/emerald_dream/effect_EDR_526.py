"""Effect for Renferal, the Malignant (EDR_526).

Card Text: [x]<b>Battlecry:</b> Trap 1 random card
in your opponent's hand for a
turn. <i>(Improved for each time
you've played this.)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass