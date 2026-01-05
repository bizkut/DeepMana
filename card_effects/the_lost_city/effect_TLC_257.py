"""Effect for Loh, the Living Legend (TLC_257).

Card Text: <b>Battlecry:</b> Your minions cost (5) this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass