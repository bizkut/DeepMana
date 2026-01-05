"""Effect for EVIL Recruiter (ULD_162).

Card Text: <b>Battlecry:</b> Destroy a friendly <b>Lackey</b> to summon a 5/5 Demon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_162t")