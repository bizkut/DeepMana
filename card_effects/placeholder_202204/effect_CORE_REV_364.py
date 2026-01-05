"""Effect for Stag Charge (CORE_REV_364).

Card Text: Deal $3 damage. Summon a random <b>Dormant</b> Wildseed.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)