"""Effect for Virmen Sensei (WON_300).

Card Text: <b>Battlecry:</b> Give a friendly Beast +3/+3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3