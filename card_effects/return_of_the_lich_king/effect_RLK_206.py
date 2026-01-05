"""Effect for Mark of Scorn (RLK_206).

Card Text: [x]Draw a card. If it's not a
minion, deal $4 damage to
the lowest Health enemy.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)