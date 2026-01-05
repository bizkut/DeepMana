"""Effect for Silvermoon Portal (WON_309).

Card Text: Give a minion +2/+2. Summon a random
2-Cost minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_309t")