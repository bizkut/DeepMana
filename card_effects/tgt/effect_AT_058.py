"""Effect for King's Elekk (AT_058).

Card Text: <b>Battlecry:</b> Reveal a minion in each deck. If yours costs more, draw it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)