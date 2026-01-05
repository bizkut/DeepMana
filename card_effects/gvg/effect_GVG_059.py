"""Effect for Coghammer (GVG_059).

Card Text: <b>Battlecry:</b> Give a random friendly minion <b>Divine Shield</b> and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1