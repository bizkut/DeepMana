"""Effect for Imprisoned Antaen (BT_934).

Card Text: [x]<b>Dormant</b> for 2 turns.
When this awakens, deal
10 damage randomly split
among all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 2, source)