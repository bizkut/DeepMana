"""Effect for Wickerclaw (SW_436).

Card Text: After your hero gains Attack, this minion
gains +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2