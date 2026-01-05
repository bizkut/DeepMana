"""Effect for Gnomeferatu (ICC_407).

Card Text: <b>Battlecry:</b> Remove
the top card of your opponent's deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass