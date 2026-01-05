"""Effect for Altruis the Outcast (BT_937).

Card Text: [x]After you play the left-
or right-most card in your
hand, deal 1 damage
to all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)