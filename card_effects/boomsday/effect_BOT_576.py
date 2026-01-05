"""Effect for Crazed Chemist (BOT_576).

Card Text: <b>Combo:</b> Give a friendly minion +4 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4