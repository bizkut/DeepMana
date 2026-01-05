"""Effect for Effigy (AT_002).

Card Text: <b>Secret:</b> When a friendly minion dies, summon a random minion with the same Cost.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AT_002t")