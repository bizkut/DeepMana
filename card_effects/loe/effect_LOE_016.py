"""Effect for Rumbling Elemental (LOE_016).

Card Text: After you play a <b>Battlecry</b> minion, deal 2 damage to a random enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 2, source)