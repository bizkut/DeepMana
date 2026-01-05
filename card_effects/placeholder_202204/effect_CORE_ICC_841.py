"""Effect for Blood-Queen Lana'thel (CORE_ICC_841).

Card Text: [x]<b>Lifesteal</b>
Has +1 Attack for each
card you've discarded
this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1