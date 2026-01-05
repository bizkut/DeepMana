"""Effect for Psyfiend (SW_445).

Card Text: After you cast a Shadow spell, deal 2 damage to each hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)