"""Effect for Prize Plunderer (DMF_519).

Card Text: [x]<b>Combo:</b> Deal 1 damage to
a minion for each other card
you've played this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)