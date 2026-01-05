"""Effect for Escaped Manasaber (YOD_006).

Card Text: [x]<b>Stealth</b>
Whenever this attacks,
gain 1 Mana Crystal
this turn only.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass