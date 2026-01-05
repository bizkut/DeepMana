"""Effect for Felfire in the Hole! (AV_281).

Card Text: Draw a spell and deal $2 damage to all enemies. If it's a Fel spell, deal $1 more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)