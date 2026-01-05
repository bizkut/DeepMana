"""Effect for Razorpetal Lasher (UNG_058).

Card Text: [x]<b>Battlecry:</b> Add a
Razorpetal to your hand
that deals 2 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)