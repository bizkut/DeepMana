"""Effect for Earthen Scales (UNG_108).

Card Text: Give a friendly minion +1/+1, then gain Armor equal to its Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1