"""Effect for Cursed Disciple (LOOT_233).

Card Text: <b>Deathrattle:</b> Summon a 5/1 Revenant.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_233t")