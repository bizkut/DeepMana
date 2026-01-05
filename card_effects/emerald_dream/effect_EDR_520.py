"""Effect for Forbidden Shrine (EDR_520).

Card Text: [x]Spend all your Mana.
Cast a random spell
that costs that much.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass