"""Effect for Dark Iron Dwarf (CORE_EX1_046).

Card Text: <b>Battlecry:</b> Give a minion +2 Attack this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2