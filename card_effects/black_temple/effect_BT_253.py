"""Effect for Psyche Split (BT_253).

Card Text: Give a minion +1/+2. Summon a copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_253t")