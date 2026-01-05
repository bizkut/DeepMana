"""Effect for Immortalized in Stone (TSC_076).

Card Text: Summon a 4/8, 2/4, and 1/2 Elemental with <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_076t")