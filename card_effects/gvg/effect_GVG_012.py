"""Effect for Light of the Naaru (GVG_012).

Card Text: Restore #3 Health. If the target is still damaged, summon a Lightwarden.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GVG_012t")