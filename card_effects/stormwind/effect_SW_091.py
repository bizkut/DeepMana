"""Effect for The Demon Seed (SW_091).

Card Text: [x]<b>Questline:</b> Take 12
damage on your turns.
<b>Reward:</b> <b>Lifesteal</b>. Deal $3
damage to the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 12, source)