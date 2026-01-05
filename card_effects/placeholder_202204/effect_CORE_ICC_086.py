"""Effect for Glacial Mysteries (CORE_ICC_086).

Card Text: Put one of each <b>Secret</b> from your deck into
the battlefield.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass