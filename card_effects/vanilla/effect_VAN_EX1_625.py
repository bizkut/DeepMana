"""Effect for Shadowform (VAN_EX1_625).

Card Text: Your Hero Power becomes 'Deal 2 damage.' If already in Shadowform: 3 damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)