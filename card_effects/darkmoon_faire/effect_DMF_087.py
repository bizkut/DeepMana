"""Effect for Trampling Rhino (DMF_087).

Card Text: <b>Rush</b>. After this attacks
and kills a minion, excess damage hits the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass