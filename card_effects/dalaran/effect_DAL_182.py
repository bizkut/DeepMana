"""Effect for Magic Dart Frog (DAL_182).

Card Text: After you cast a spell, deal 1 damage to a random enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 1, source)