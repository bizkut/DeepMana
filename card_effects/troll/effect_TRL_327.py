"""Effect for Spirit of the Rhino (TRL_327).

Card Text: <b>Stealth</b> for 1 turn.
Your <b>Rush</b> minions are <b>Immune</b> the turn they're summoned.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_327t")