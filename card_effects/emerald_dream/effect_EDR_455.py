"""Effect for Succumb to Madness (EDR_455).

Card Text: <b>Discover</b> a friendly Dragon that died this game. Resummon it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_455t")