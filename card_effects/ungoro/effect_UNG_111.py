"""Effect for Living Mana (UNG_111).

Card Text: Transform your Mana Crystals into 2/2 Treants. Recover the mana when they die.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass