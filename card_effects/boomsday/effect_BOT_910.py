"""Effect for Glowstone Technician (BOT_910).

Card Text: <b>Battlecry:</b> Give all minions in your hand +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2