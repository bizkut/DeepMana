"""Effect for Hadronox (ICC_835).

Card Text: <b>Deathrattle:</b> Summon your <b>Taunt</b> minions that
died this game.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ICC_835t")