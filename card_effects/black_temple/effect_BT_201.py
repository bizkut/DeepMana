"""Effect for Augmented Porcupine (BT_201).

Card Text: [x]<b>Deathrattle</b>: Deal this
minion's Attack damage
randomly split among
all enemies.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 1, source)