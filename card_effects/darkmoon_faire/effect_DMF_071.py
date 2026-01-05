"""Effect for Tenwu of the Red Smoke (DMF_071).

Card Text: <b>Battlecry:</b> Return a friendly minion to your hand. It costs (1) this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass