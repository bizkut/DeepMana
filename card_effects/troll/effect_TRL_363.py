"""Effect for Saronite Taskmaster (TRL_363).

Card Text: <b>Deathrattle:</b> Summon a 0/3 Free Agent with <b>Taunt</b> for your opponent.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_363t")