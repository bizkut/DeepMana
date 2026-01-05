"""Effect for Shadowcaster (OG_291).

Card Text: <b>Battlecry:</b> Choose a friendly minion. Add a 1/1 copy to your hand that costs (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass