"""Effect for Gurubashi Chicken (TRL_506).

Card Text: <b>Overkill:</b> Gain +5 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5