"""Effect for Sudden Genesis (UNG_927).

Card Text: Summon copies of your damaged minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_927t")