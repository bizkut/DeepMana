"""Effect for Veiled Worshipper (DRG_203).

Card Text: [x]<b>Battlecry:</b> If you've <b>Invoked</b>
twice, draw 3 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)