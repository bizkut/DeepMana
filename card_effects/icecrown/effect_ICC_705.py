"""Effect for Bonemare (ICC_705).

Card Text: <b>Battlecry:</b> Give a friendly minion +4/+4 and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4