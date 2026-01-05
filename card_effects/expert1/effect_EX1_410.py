"""Effect for Shield Slam (EX1_410).

Card Text: Deal 1 damage to a minion for each Armor you have.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)