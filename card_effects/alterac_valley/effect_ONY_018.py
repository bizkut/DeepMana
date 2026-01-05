"""Effect for Boomkin (ONY_018).

Card Text: <b>Choose One - </b>Restore
8 Health to your hero; or Deal 4 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 8, source)