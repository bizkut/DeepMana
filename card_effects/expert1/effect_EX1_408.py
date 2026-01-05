"""Effect for Mortal Strike (EX1_408).

Card Text: Deal $4 damage. If you have 12 or less Health, deal $6 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)