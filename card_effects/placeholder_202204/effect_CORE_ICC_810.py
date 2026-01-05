"""Effect for Deathaxe Punisher (CORE_ICC_810).

Card Text: <b>Battlecry:</b> Give a random <b>Lifesteal</b> minion in your hand +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2