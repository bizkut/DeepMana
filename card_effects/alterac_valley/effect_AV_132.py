"""Effect for Troll Centurion (AV_132).

Card Text: [x]<b>Rush</b>. <b>Honorable Kill:</b>
Deal 8 damage to the
enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 8, source)