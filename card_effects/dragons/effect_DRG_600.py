"""Effect for Galakrond, the Wretched (DRG_600).

Card Text: [x]<b>Battlecry:</b> Summon
1 random Demon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_600t")