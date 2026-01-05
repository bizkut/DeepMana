"""Effect for Phalanx Commander (ULD_179).

Card Text: Your <b>Taunt</b> minions
have +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2