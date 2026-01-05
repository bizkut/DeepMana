"""Effect for Tip the Scales (ULD_716).

Card Text: Summon 7 Murlocs from your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_716t")