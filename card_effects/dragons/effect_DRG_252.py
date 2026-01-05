"""Effect for Phase Stalker (DRG_252).

Card Text: [x]After you use your Hero
Power, cast a <b>Secret</b>
from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass