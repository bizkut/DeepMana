"""Effect for Sword and Board (BT_233).

Card Text: Deal $2 damage to a minion. Gain 2 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)