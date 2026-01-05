"""Effect for Metaltooth Leaper (GVG_048).

Card Text: <b>Battlecry:</b> Give your other Mechs +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2