"""Effect for Keeper of the Grove (EX1_166).

Card Text: <b>Choose One -</b> Deal 2 damage; or <b>Silence</b> a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)