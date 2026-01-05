"""Effect for Conceal (EX1_128).

Card Text: Give your minions <b>Stealth</b> until your next turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1