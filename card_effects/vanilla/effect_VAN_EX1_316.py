"""Effect for Power Overwhelming (VAN_EX1_316).

Card Text: Give a friendly minion +4/+4 until end of turn. Then, it dies. Horribly.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4