"""Effect for Collateral Damage (CORE_REV_369).

Card Text: [x]Deal $6 damage to three 
random enemy minions. 
Excess damage hits 
the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 6, source)