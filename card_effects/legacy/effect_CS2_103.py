"""Effect for Charge (CS2_103).

Card Text: Give a friendly minion +2 Attack and <b>Charge</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2