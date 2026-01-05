"""Effect for Deck of Chaos (DMF_534).

Card Text: Swap the Cost and Attack of all minions in your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass