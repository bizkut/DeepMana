"""Effect for Perpetual Flame (WC_020).

Card Text: Deal $3 damage to a random enemy minion. If it dies, recast this. <b>Overload:</b> (1)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)