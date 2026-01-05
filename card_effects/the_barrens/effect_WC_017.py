"""Effect for Savory Deviate Delight (WC_017).

Card Text: [x]Transform a minion in
both players' hands into a
Pirate or <b>Stealth</b> minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass