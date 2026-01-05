"""Effect for Shellshot (TID_075).

Card Text: [x]Deal $3 damage to a
random enemy minion.
Repeat this with 1
less damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)