"""Effect for Ship's Cannon (GVG_075).

Card Text: [x]After you summon a
Pirate, deal 2 damage
to a random enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 2, source)