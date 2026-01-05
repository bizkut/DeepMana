"""Effect for Ironhide Direhorn (TRL_232).

Card Text: <b>Overkill:</b> Summon a 5/5 Ironhide Runt.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_232t")