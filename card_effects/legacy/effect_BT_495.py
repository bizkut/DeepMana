"""Effect for Glaivebound Adept (BT_495).

Card Text: <b>Battlecry:</b> If your hero attacked this turn,
deal 4 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)