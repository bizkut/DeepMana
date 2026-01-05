"""Effect for Queen Azshara (TSC_641).

Card Text: <b>Battlecry:</b> If you've cast three spells while holding this, choose an Ancient Relic.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass