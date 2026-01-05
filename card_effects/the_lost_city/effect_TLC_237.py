"""Effect for Skyscreamer Eggs (TLC_237).

Card Text: <b>Deathrattle:</b> Summon four 2/1 Hatchlings.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_237t")