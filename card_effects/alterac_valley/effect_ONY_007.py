"""Effect for Haleh, Matron Protectorate (ONY_007).

Card Text: After you cast a spell, deal 4 damage randomly split among all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 4, source)