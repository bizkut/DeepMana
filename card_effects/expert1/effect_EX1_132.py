"""Effect for Eye for an Eye (EX1_132).

Card Text: <b>Secret:</b> When your hero takes damage, deal that much damage to the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)