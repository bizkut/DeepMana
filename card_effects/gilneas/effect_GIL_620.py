"""Effect for Dollmaster Dorian (GIL_620).

Card Text: Whenever you draw a minion, summon a 1/1 copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)