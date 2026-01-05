"""Effect for Brasswing (AV_340).

Card Text: [x]At the end of your turn, deal
2 damage to all enemies.
<b>Honorable Kill:</b> Restore 4
Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)