"""Effect for Mr. Smite (DED_006).

Card Text: Your Pirates have <b>Charge</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass