"""Effect for Imp Swarm (Rank 1) (BAR_914).

Card Text: Summon a 3/2 Imp. <i>(Upgrades when you have 5 Mana.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_914t")