"""Effect for Bloodlust (CS2_046).

Card Text: Give your minions +3 Attack this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3