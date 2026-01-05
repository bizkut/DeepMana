"""Effect for Tar Tyrant (TLC_605).

Card Text: [x]<b>Taunt</b>, <b>Lifesteal</b>
Has +6 Attack during your
opponent's turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 6
        target._max_health += 6