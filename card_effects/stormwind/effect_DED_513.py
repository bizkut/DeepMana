"""Effect for Defias Leper (DED_513).

Card Text: [x]<b>Battlecry:</b> If you're holding
a Shadow spell, deal
2 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)