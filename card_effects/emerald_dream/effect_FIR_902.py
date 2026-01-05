"""Effect for Sigil of Cinder (FIR_902).

Card Text: [x]At the start of your next
turn, deal $6 damage
randomly split among
all enemies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 6, source)