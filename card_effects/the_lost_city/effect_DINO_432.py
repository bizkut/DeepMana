"""Effect for Panther Mask (DINO_432).

Card Text: Set a minion's stats to
5/4 and give it <b>Stealth</b>. Draw 2 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)