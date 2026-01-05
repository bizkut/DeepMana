"""Effect for Gorishi Tunneler (TLC_840).

Card Text: <b>Stealth</b>
After this attacks,
deal 2 damage to the
enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)