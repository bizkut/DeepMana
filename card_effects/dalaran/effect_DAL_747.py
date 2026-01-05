"""Effect for Flight Master (DAL_747).

Card Text: <b>Battlecry:</b> Summon a 2/2 Gryphon for each player.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_747t")