"""Effect for Footman (CORE_TOY_102).

Card Text: <b>Taunt</b>
Adjacent minions are <b>Immune</b> while attacking.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass