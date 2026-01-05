"""Effect for Twilight Drake (EX1_043).

Card Text: <b>Battlecry:</b> Gain +1 Health for each card in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)