"""Effect for Chittering Tunneler (UNG_835).

Card Text: [x]<b>Battlecry:</b> <b>Discover</b> a spell.
Deal damage to your hero
equal to its Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)