"""Effect for Fossilized Devilsaur (LOE_073).

Card Text: <b>Battlecry:</b> If you control another Beast, gain <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass