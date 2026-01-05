"""Effect for Umbral Owl (CORE_DMF_060).

Card Text: [x]<b>Rush</b>
Costs (1) less for each spell
you've cast this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass