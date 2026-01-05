"""Effect for Bomb Toss (BOT_033).

Card Text: Deal $2 damage. Summon a 0/2 Goblin Bomb.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)