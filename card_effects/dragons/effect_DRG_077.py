"""Effect for Utgarde Grapplesniper (DRG_077).

Card Text: <b>Battlecry:</b> Both players draw a card. If it's a Dragon, summon it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)