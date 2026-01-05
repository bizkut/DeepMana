"""Effect for Star Student Stelina (SCH_603).

Card Text: [x]<b>Outcast:</b> Look at 3 cards
in your opponent's hand.
Shuffle one of them
into their deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass