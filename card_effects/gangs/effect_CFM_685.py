"""Effect for Don Han'Cho (CFM_685).

Card Text: <b>Battlecry:</b> Give a
random minion in your hand +5/+5.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5