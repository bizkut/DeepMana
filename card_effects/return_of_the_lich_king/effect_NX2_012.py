"""Effect for Rake (NX2_012).

Card Text: [x]Give your hero +2 Attack
this turn. Deal damage
equal to your hero's
Attack to a minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)