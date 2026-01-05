"""Effect for Breath of Sindragosa (CORE_ICC_836).

Card Text: Deal $2 damage to a random enemy minion and <b>Freeze</b> it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 2, source)