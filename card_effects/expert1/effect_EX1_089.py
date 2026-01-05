"""Effect for Arcane Golem (EX1_089).

Card Text: <b>Charge</b>. <b>Battlecry:</b> Give your opponent a Mana Crystal.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1