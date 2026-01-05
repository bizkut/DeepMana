"""Effect for Underbrush Tracker (TLC_520).

Card Text: [x]<b>Rush</b>
Costs (1) less for each
time you've shuffled cards
into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass