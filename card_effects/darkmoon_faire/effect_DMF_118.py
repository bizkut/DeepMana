"""Effect for Tickatus (DMF_118).

Card Text: [x]<b>Battlecry:</b> Remove the
top 5 cards from your deck.
<b>Corrupt:</b> Your opponent's
deck instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass