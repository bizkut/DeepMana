"""Effect for Flames of the Firelord (FIR_923).

Card Text: [x]Deal $4 damage to a random
enemy minion. If you're
holding a card that costs
(8) or more, deal $8 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 4, source)