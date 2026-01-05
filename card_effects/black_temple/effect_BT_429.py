"""Effect for Metamorphosis (BT_429).

Card Text: Swap your Hero Power to "Deal 5 damage." After 2 uses, swap it back.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)