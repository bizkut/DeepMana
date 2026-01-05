"""Effect for Toxicologist (BOT_083).

Card Text: <b>Battlecry:</b> Give your weapon +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1