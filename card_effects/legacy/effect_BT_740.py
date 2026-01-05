"""Effect for Soul Cleave (BT_740).

Card Text: <b>Lifesteal</b>
Deal $2 damage to two random enemy minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 2, source)