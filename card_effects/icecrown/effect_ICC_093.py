"""Effect for Tuskarr Fisherman (ICC_093).

Card Text: <b>Battlecry:</b> Give a friendly minion <b>Spell Damage +1</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1