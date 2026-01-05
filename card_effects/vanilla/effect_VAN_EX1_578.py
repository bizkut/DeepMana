"""Effect for Savagery (VAN_EX1_578).

Card Text: Deal damage equal to your hero's Attack to a minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)