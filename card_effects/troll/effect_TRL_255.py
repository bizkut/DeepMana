"""Effect for Stampeding Roar (TRL_255).

Card Text: Summon a random Beast from your hand and give it <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_255t")