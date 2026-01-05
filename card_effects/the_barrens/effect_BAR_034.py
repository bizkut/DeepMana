"""Effect for Tame Beast (Rank 1) (BAR_034).

Card Text: Summon a 2/2 Beast with <b>Rush</b>. <i>(Upgrades when you
have 5 Mana.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_034t")