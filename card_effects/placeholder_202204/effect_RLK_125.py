"""Effect for Obliterate (RLK_125).

Card Text: Destroy a minion. Deal 3 damage to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)