"""Effect for Bonechewer Raider (BT_140).

Card Text: <b>Battlecry:</b> If there is a damaged minion, gain +1/+1 and <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1