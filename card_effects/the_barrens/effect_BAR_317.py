"""Effect for Field Contact (BAR_317).

Card Text: [x]After you play a <b>Battlecry</b>
or <b>Combo</b> card, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)