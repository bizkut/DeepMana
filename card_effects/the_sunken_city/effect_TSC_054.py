"""Effect for Mecha-Shark (TSC_054).

Card Text: [x]After you summon a Mech,
deal 3 damage randomly
 split among all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)