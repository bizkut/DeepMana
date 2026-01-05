"""Effect for Relentless Pursuit (DMF_219).

Card Text: Give your hero +4 Attack and <b>Immune</b> this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4