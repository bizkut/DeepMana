"""Effect for Spirit Bomb (BOT_222).

Card Text: Deal $4 damage to a minion and your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)