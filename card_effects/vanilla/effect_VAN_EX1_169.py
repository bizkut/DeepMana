"""Effect for Innervate (VAN_EX1_169).

Card Text: Gain 2 Mana Crystals this turn only.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass