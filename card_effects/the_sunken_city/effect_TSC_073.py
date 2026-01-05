"""Effect for Raj Naz'jan (TSC_073).

Card Text: After you cast a spell, deal damage equal to its Cost to the enemy Hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)