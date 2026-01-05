"""Effect for Raging Felscreamer (BT_416).

Card Text: <b>Battlecry:</b> The next Demon you play costs (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass