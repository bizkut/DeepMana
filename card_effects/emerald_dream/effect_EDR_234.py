"""Effect for Emerald Bounty (EDR_234).

Card Text: Draw 2 cards.
You can't play them
for 2 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)