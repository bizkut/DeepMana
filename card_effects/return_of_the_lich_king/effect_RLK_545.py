"""Effect for Energy Shaper (RLK_545).

Card Text: [x]<b>Battlecry:</b> Transform all
spells in your hand into ones
that cost (3) more. <i>(They keep
their original Cost.)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass