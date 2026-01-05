"""Effect for Innervate (EX1_169).

Card Text: Gain 1 Mana Crystal this turn only.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass