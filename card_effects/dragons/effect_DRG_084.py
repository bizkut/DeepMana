"""Effect for Tentacled Menace (DRG_084).

Card Text: <b>Battlecry:</b> Each player draws a card. Swap their Costs.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)