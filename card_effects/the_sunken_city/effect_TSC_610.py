"""Effect for Glaiveshark (TSC_610).

Card Text: [x]<b>Battlecry:</b> If your hero
attacked this turn, deal 2
damage to all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)