"""Effect for Plague Scientist (ICC_809).

Card Text: <b>Combo:</b> Give a friendly minion <b>Poisonous</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1