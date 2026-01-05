"""Effect for Umbral Skulker (DRG_027).

Card Text: [x]<b>Battlecry:</b> If you've <b>Invoked</b>
twice, add 3 Coins to
your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass