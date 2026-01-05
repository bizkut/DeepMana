"""Effect for Venomstrike Trap (ICC_200).

Card Text: <b>Secret:</b> When one of your minions is attacked, summon a 2/3 <b>Poisonous</b> Cobra.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ICC_200t")