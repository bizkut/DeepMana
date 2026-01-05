"""Effect for Remornia, Living Blade (REV_316).

Card Text: <b>Rush</b>
After this attacks, equip it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass