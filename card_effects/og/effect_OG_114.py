"""Effect for Forbidden Ritual (OG_114).

Card Text: Spend all your Mana. Summon that many 1/1 Tentacles.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_114t")