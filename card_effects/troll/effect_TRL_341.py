"""Effect for Treespeaker (TRL_341).

Card Text: <b>Battlecry:</b> Transform your Treants into 5/5 Ancients.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass