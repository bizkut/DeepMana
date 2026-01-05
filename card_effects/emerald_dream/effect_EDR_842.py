"""Effect for Defiled Spear (EDR_842).

Card Text: [x]After your hero attacks an
 enemy, deal your hero's
Attack damage to another
random enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 1, source)