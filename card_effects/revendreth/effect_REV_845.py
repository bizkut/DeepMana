"""Effect for Volatile Skeleton (REV_845).

Card Text: <b>Deathrattle:</b> Deal 2 damage to a random enemy.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 2, source)