"""Effect for Violet Wurm (LOOT_153).

Card Text: <b>Deathrattle:</b> Summon seven 1/1 Grubs.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_153t")