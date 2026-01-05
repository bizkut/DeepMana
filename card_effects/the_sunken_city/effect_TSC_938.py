"""Effect for Treasure Guard (TSC_938).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Draw a card.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)