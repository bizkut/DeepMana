"""Effect for Envoy of Lazul (DRG_306).

Card Text: [x]<b>Battlecry:</b> Look at 3 cards.
Guess which one is in
your opponent's hand
to get a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass