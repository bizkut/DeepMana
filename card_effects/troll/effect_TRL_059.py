"""Effect for Bog Slosher (TRL_059).

Card Text: <b>Battlecry:</b> Return a friendly minion to your hand and give it +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2