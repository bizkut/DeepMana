"""Effect for Demonic Project (BOT_913).

Card Text: Each player transforms a random minion in their hand into a Demon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass