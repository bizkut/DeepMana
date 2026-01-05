"""Effect for Sightless Watcher (BT_323).

Card Text: <b>Battlecry:</b> Look at 3 cards in your deck. Choose one to put on top.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass