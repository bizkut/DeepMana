"""Effect for Chopshop Copter (YOD_004).

Card Text: After a friendly Mech dies, add a random Mech to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass