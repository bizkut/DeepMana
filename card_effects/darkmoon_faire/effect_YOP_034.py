"""Effect for Runaway Blackwing (YOP_034).

Card Text: [x]At the end of your turn,
deal 10 damage to a
random enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 10, source)