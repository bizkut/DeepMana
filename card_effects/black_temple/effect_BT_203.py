"""Effect for Pack Tactics (BT_203).

Card Text: <b>Secret:</b> When a friendly minion is attacked, summon a 3/3 copy.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_203t")