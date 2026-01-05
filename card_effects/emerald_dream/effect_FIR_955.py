"""Effect for Emberroot Destroyer (FIR_955).

Card Text: [x]Whenever your hero takes
damage on your turn,
deal 3 damage to a random
enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)