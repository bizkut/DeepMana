"""Effect for Turalyon, the Tenured (SCH_135).

Card Text: [x]<b>Rush</b>. Whenever this attacks
a minion, set the defender's
Attack and Health to 3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)