"""Effect for King of Beasts (WON_162).

Card Text: [x]<b>Taunt</b>
Has +1 Attack for each
other Beast you control.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1