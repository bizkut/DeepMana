"""Effect for Soul Shear (SCH_701).

Card Text: [x]Deal $3 damage to a
minion. Shuffle 2 Soul
Fragments into your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)