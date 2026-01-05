"""Effect for Hadronox (CORE_ICC_835).

Card Text: <b>Deathrattle:</b> Summon your <b>Taunt</b> minions that
died this game.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_ICC_835t")