"""Effect for Shadow Sensei (CFM_694).

Card Text: <b>Battlecry:</b> Give a <b>Stealthed</b> minion +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2