"""Effect for Humongous Owl (AV_704).

Card Text: <b>Deathrattle:</b> Deal 8 damage to a random enemy.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 8, source)