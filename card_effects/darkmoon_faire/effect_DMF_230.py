"""Effect for Il'gynoth (DMF_230).

Card Text: [x]<b>Lifesteal</b>
Your <b>Lifesteal</b> damages
the enemy hero instead
of healing you.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)