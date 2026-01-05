"""Effect for Argent Lance (AT_077).

Card Text: <b>Battlecry:</b> Reveal a minion in each deck. If yours costs more, +1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1