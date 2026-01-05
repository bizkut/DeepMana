"""Effect for Overconfident Orc (BT_730).

Card Text: <b>Taunt</b>
While at full Health,
this has +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)