"""Effect for Spectral Pillager (CORE_ICC_910).

Card Text: [x]<b>Combo:</b> Deal damage equal
to the number of other cards
you've played this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)