"""Effect for Inara Stormcrash (DMF_708).

Card Text: On your turn, your hero has +2 Attack and <b>Windfury</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2