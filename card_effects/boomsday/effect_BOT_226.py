"""Effect for Nethersoul Buster (BOT_226).

Card Text: <b>Battlecry:</b> Gain +1 Attack for each damage your hero has taken this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1