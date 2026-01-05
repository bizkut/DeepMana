"""Effect for Splitting Axe (ULD_413).

Card Text: <b>Battlecry:</b> Summon copies of your Totems.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_413t")