"""Effect for Atlasaurus (DINO_431).

Card Text: <b>Taunt</b>. <b>Deathrattle:</b> Summon a random <b>Taunt</b> minion that costs (5) or more.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DINO_431t")