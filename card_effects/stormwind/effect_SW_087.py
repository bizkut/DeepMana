"""Effect for Dreaded Mount (SW_087).

Card Text: [x]Give a minion +1/+1.
When it dies, summon
an endless Dreadsteed.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_087t")