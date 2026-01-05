"""Effect for Rain of Toads (TRL_351).

Card Text: Summon three 2/4 Toads with <b>Taunt</b>. <b>Overload:</b> (3)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_351t")