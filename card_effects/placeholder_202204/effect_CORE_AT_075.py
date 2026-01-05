"""Effect for Warhorse Trainer (CORE_AT_075).

Card Text: Your Silver Hand Recruits have +2 Attack and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2