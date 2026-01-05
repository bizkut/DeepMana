"""Effect for Relic of Extinction (CORE_REV_834).

Card Text: Deal $1 damage to a random enemy minion, twice. Improve your future Relics.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 1, source)