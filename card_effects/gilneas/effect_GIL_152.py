"""Effect for Blackhowl Gunspire (GIL_152).

Card Text: [x]Can't attack. Whenever
this minion takes damage,
deal 3 damage to a
random enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)