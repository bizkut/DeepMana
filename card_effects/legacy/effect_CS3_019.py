"""Effect for Kor'vas Bloodthorn (CS3_019).

Card Text: [x]<b>Charge</b>, <b>Lifesteal</b>
After you play a card with
<b>Outcast</b>, return this to
your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass