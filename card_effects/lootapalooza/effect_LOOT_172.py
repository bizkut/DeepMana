"""Effect for Dragon's Fury (LOOT_172).

Card Text: Reveal a spell from your deck. Deal damage equal to its Cost to all minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)