"""Effect for Crimson Hothead (SCH_232).

Card Text: <b>Spellburst:</b> Gain +1 Attack and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1