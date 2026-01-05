"""Effect for Bloodied Knight (RLK_926).

Card Text: [x]At the end of your turn,
deal 2 damage to
your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)