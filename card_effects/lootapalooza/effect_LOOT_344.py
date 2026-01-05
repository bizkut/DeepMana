"""Effect for Primal Talismans (LOOT_344).

Card Text: Give your minions "<b>Deathrattle:</b> Summon a random basic Totem."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_344t")