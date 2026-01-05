"""Effect for Commander Ulthok (TID_719).

Card Text: <b>Battlecry:</b> Your opponent's cards cost Health instead of Mana next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)