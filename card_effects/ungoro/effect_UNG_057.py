"""Effect for Razorpetal Volley (UNG_057).

Card Text: Add two Razorpetals to your hand that deal 2 damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)