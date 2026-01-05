"""Effect for Noble Mount (SW_316).

Card Text: G[x]ive a minion +1/+1
and <b>Divine Shield</b>.
When it dies, summon
a Warhorse.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_316t")