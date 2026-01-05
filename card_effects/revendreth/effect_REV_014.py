"""Effect for Red Herring (REV_014).

Card Text: [x]<b>Taunt</b>
Your non-Red Herring
minions have <b>Stealth</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass