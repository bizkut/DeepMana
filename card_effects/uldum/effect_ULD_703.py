"""Effect for Desert Obelisk (ULD_703).

Card Text: [x]If you control 3 of these
at the end of your turn,
deal 5 damage to a
random enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)