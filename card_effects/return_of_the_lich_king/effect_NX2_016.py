"""Effect for Nofin's Imp-ossible (NX2_016).

Card Text: Give all friendly Demons and Murlocs "<b>Deathrattle:</b> Summon a 2/2 Imploc."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "NX2_016t")