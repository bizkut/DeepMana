"""Effect for Camouflaged Dirigible (DRG_074).

Card Text: <b>Battlecry:</b> Give your other Mechs <b>Stealth</b> until your next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1