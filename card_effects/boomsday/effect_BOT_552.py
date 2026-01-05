"""Effect for Star Aligner (BOT_552).

Card Text: [x]<b>Battlecry:</b> If you control 3
minions with 7 Health, deal
7 damage to all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)