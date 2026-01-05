"""Effect for Fist of Jaraxxus (AT_022).

Card Text: When you play or discard this, deal $4 damage to a random enemy.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 4, source)