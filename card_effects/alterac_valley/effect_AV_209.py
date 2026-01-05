"""Effect for Dreadprison Glaive (AV_209).

Card Text: [x]<b>Honorable Kill:</b> Deal
damage equal to your
hero's Attack to the
enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)