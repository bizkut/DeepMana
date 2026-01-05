"""Effect for Soul of the Murloc (DAL_710).

Card Text: Give your minions "<b>Deathrattle:</b> Summon a 1/1 Murloc."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_710t")