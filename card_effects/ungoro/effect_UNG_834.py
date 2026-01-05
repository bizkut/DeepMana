"""Effect for Feeding Time (UNG_834).

Card Text: Deal $3 damage to a minion. Summon three 1/1 Pterrordaxes and <b>Adapt</b> them.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)