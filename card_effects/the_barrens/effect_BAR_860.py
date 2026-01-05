"""Effect for Firemancer Flurgl (BAR_860).

Card Text: [x]After you play a Murloc,
deal 1 damage to
all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)