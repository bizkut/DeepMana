"""Effect for Glugg the Gulper (TSC_639).

Card Text: [x]<b>Colossal +3</b>
 After a friendly minion dies,
gain its original stats.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3