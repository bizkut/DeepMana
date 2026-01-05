"""Effect for Crushclaw Enforcer (TSC_826).

Card Text: <b>Battlecry:</b> If you've cast
 a spell while holding this, draw a Naga.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)