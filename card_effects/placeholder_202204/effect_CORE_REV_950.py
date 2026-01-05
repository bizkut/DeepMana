"""Effect for Divine Toll (CORE_REV_950).

Card Text: [x]Shoot 5 rays at random
minions. They give friendly
minions +2/+2, and deal $2
damage to enemy minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 5, source)