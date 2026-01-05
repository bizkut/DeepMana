"""Effect for A New Challenger... (TRL_305).

Card Text: <b>Discover</b> a 6-Cost minion. Summon it with <b>Taunt</b> and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_305t")