"""Effect for Grand Archivist (LOOT_414).

Card Text: At the end of your turn, cast a spell from your deck <i>(targets chosen randomly)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass