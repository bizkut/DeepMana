"""Effect for Ymirjar Frostbreaker (RLK_110).

Card Text: <b>Battlecry:</b> Gain +1 Attack for each Frost spell
in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1