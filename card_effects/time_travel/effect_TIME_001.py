"""Effect for Chrono Daggers (TIME_001).

Card Text: <b>Rewind</b>
Throw 3 knives at
random enemies that deal $2 damage each.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)